# Bot de Gestión de Inventario para Telegram 🛒🤖

Este es un bot de Telegram diseñado para gestionar el inventario de una tienda. Permite agregar, listar y eliminar productos de manera sencilla y eficiente.
## Funcionalidades principales 🚀

El bot cuenta con los siguientes comandos:

### 1. **/start**
Inicia el bot y muestra un mensaje de bienvenida.


````
/start
````

¡Hola [nombre]! 👋 Soy tu bot de gestión de inventario. Usa /add para agregar productos y /list para ver el inventario.


(La funcionalidad /delete está oculta solo para el administrador del stock, por eso no aparece a la hora de informar sobre las funcionalidades.)


### 2. **/add `<nombre>` `<cantidad>` `<precio>`**
Agrega un nuevo producto al inventario.
- **Ejemplo:**

````
/add pera 10 2.5
````

- **Respuesta:**

✅ Producto 'pera' agregado al inventario.
📦 Cantidad: 10
💰 Precio: $2.5


**Nota:** No se permiten productos con el mismo nombre pero diferente precio. Si el producto ya existe, se actualiza la cantidad, y si intentas añadir uno con mismo nombre pero distinto precio te da error.

### 3. **/list**
Muestra todos los productos en el inventario.
- **Ejemplo:**

```
/list
```

- **Respuesta:**

📋 Inventario:

📦 Producto: pera
🔢 Cantidad: 10
💰 Precio: $2.5


### 4. **/delete `<nombre_producto>`**
Elimina un producto del inventario.
- **Ejemplo:**

```
/delete pera
```

- **Respuesta:**

✅ Producto 'pera' eliminado del inventario.


## Requisitos 📋

Para ejecutar este bot, necesitas:

1. **Python 3.8 o superior**.
2. **Librerías necesarias**:
    - `python-telegram-bot`
    - `firebase-admin`
    - `python-dotenv`

    En caso de carecer de ellas, debes instalarlas con el siguiente comando por terminal:

    ```bash
    pip install python-telegram-bot firebase-admin python-dotenv
    ```

3. **Credenciales de Firebase:**

    - Un archivo JSON con las credenciales de Firebase.

    - Configura las credenciales en el archivo .env:  

    ```
    FIREBASE_CREDENTIALS="ruta/al/archivo.json"
    TELEGRAM_TOKEN="tu_token_de_telegram"
    ```

## Configuración ⚙️

1. Clona este repositorio o descarga el código.

2. Crea un archivo .env en la raíz del proyecto y añade tus credenciales:

    ```
    FIREBASE_CREDENTIALS="ruta/al/archivo.json"
    TELEGRAM_TOKEN="tu_token_de_telegram"
    ```
3. Ejecuta el bot:

## Ejecución ▶️

Una vez configurado, el bot estará listo para recibir comandos en Telegram. Simplemente abre una conversación con el bot y comienza a gestionar tu inventario.

## Capturas de pantalla 📸

### /start

![](/assets/start.png)

### /list

Aqui tenia el objeto del ejemplo añadido, por lo que salia ya el objeto 'pera'.

![](/assets/listProducto.png)

Si el inventario está vacío muestra este mensaje:

![](/assets/listVacio.png)

### /add

Si pones solo /add, te salta esta ayuda:

![](/assets/addAyuda.png)

Si añades correctamente un producto, por ejemplo un macbook, el mensaje seria el siguiente:

![](/assets/addProducto.png)

si intentas añadir un producto que ya esta en el inventario con otro precio, lo detectará como error, mostrando este mensaje:

![](/assets/addError.png)

Y cuando haces un add con el nombre y la cantidad, o el nombre la cantidad y el mismo precio, se actualiza el stock de dicho producto.

![](/assets/addActualizacion.png)

### /delete

Cuando eliminamos un objeto, por ejemplo el macbook, nos muestra este mensaje:

![](/assets/delete.png)

Si intentamos eliminar un objeto que no esta en nuestro inventario, muestra este mensaje:

![](/assets/deleteError.png)

### Y esto sería todo.
