import logging
import firebase_admin
from firebase_admin import credentials, firestore
from telegram import Update
from telegram.ext import CommandHandler, Application, ContextTypes
import os
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Inicializar el bot con el token de Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
FIREBASE_CREDENTIALS = os.getenv("FIREBASE_CREDENTIALS")

# Inicialización de Firebase
cred = credentials.Certificate(FIREBASE_CREDENTIALS)
firebase_admin.initialize_app(cred)
db = firestore.client()

# Habilitar el registro para debugging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Comando /start para iniciar el bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("Usuario %s ha comenzado el bot.", user.first_name)
    await update.message.reply_text(f"¡Hola {user.first_name}! 👋 Soy tu bot de gestión de inventario. Usa /add para agregar productos y /list para ver el inventario.")

# Comando /add para agregar un producto al inventario
async def add_inventory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 3:
        await update.message.reply_text("❌ Uso correcto: /add <nombre> <cantidad> <precio>")
        return
    
    name = context.args[0]
    try:
        quantity = int(context.args[1])
        price = float(context.args[2])
    except ValueError:
        await update.message.reply_text("❌ La cantidad y el precio deben ser números válidos.")
        return
    
    try:
        # Verificar si el producto ya existe en Firestore
        existing_products = db.collection('inventario').where('name', '==', name).stream()
        existing_products_list = list(existing_products)
        
        if existing_products_list:
            # Si el producto ya existe, verificar si el precio es diferente
            existing_product = existing_products_list[0].to_dict()
            existing_price = existing_product['price']
            
            if existing_price != price:
                await update.message.reply_text(
                    f"❌ El producto '{name}' ya existe con un precio diferente (${existing_price}).\n"
                    f"No se puede agregar con un nuevo precio (${price})."
                )
                return  # Salir de la función sin agregar el producto
            
            # Si el precio es el mismo, actualizar la cantidad
            product_ref = existing_products_list[0].reference
            current_quantity = existing_product['quantity']
            new_quantity = current_quantity + quantity
            
            product_ref.update({'quantity': new_quantity})
            await update.message.reply_text(
                f"🔄 Producto '{name}' actualizado.\n"
                f"📦 Nueva cantidad: {new_quantity}\n"
                f"💰 Precio: ${price}"
            )
        else:
            # Si no existe, agregar el producto a Firestore
            db.collection('inventario').add({
                'name': name,
                'quantity': quantity,
                'price': price
            })
            await update.message.reply_text(
                f"✅ Producto '{name}' agregado al inventario.\n"
                f"📦 Cantidad: {quantity}\n"
                f"💰 Precio: ${price}"
            )
    
    except Exception as e:
        await update.message.reply_text(f"❌ Hubo un error al agregar el producto: {e}")


# Comando /list para listar todos los productos del inventario
async def list_inventory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Recuperamos todos los productos de la colección 'inventario'
        products = db.collection('inventario').stream()
        products_list = list(products)

        # Si no se encuentran productos
        if not products_list:
            await update.message.reply_text("📭 El inventario está vacío.")
            return

        # Mostrar el inventario con un formato visual
        inventory_list = "📋 **Inventario:**\n\n"
        for product in products_list:
            product_data = product.to_dict()
            inventory_list += (
                f"📦 **Producto:** {product_data['name']}\n"
                f"🔢 **Cantidad:** {product_data['quantity']}\n"
                f"💰 **Precio:** ${product_data['price']}\n"
                "------------------------\n"
            )

        # Mostrar el inventario completo
        await update.message.reply_text(inventory_list)

    except Exception as e:
        await update.message.reply_text(f"❌ Hubo un error al listar los productos: {e}")


# Comando /delete para eliminar un producto del inventario
async def delete_inventory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 1:
        await update.message.reply_text("❌ Uso correcto: /delete <nombre_producto>")
        return

    name = context.args[0]
    
    # Buscar el producto en Firestore
    products = db.collection('inventario').where('name', '==', name).stream()
    deleted = False
    
    for product in products:
        product.reference.delete()
        deleted = True
    
    if deleted:
        await update.message.reply_text(f"✅ Producto '{name}' eliminado del inventario.")
    else:
        await update.message.reply_text(f"❌ Producto '{name}' no encontrado.")

# Función principal para ejecutar el bot
def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Registrar los comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("add", add_inventory))
    application.add_handler(CommandHandler("list", list_inventory))
    application.add_handler(CommandHandler("delete", delete_inventory))

    # Iniciar el bot
    application.run_polling()

if __name__ == '__main__':
    main()
