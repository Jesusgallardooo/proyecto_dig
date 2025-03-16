# Preguntas:

### Ciclo de vida del dato (5b):
- ¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?

Los datos se generan cuando un usuario agrega un producto con /add, se almacenan en Firestore, se consultan con /list, se actualizan al agregar más cantidad de un producto existente y se eliminan con /delete. Cada paso incluye validaciones para garantizar que los datos sean correctos y consistentes.

- ¿Qué estrategia sigues para garantizar la consistencia e integridad de los datos? Si no trabajas con datos, ¿cómo podrías incluir una funcionalidad que los gestione de forma eficiente?

Se validan los datos antes de agregarlos (cantidad y precio deben ser números), se evitan duplicados con precios diferentes y se actualizan las cantidades en lugar de crear registros repetidos. Además, Firestore asegura la integridad y consistencia de los datos a nivel de base de datos.


### Almacenamiento en la nube (5f):
- Si tu software utiliza almacenamiento en la nube, ¿cómo garantizas la seguridad y disponibilidad de los datos?

El proyecto utiliza Firestore de Firebase como almacenamiento en la nube. La seguridad se garantiza mediante reglas de Firestore, que controlan quién puede leer o escribir datos, y autenticación de usuarios. La disponibilidad es alta, ya que Firestore es un servicio gestionado por Google, con redundancia y backups automáticos.

- ¿Qué alternativas consideraste para almacenar datos y por qué elegiste tu solución actual? Si no usas la nube, ¿cómo podrías integrarla en futuras versiones?

Se consideraron alternativas como SQLite (para almacenamiento local) y MongoDB (para bases de datos NoSQL). Se eligió Firestore por su integración sencilla con Firebase, su escalabilidad automática y su capacidad para manejar datos en tiempo real, lo que es ideal para un bot de Telegram.

### Seguridad y regulación (5i):
- ¿Qué medidas de seguridad implementaste para proteger los datos o procesos en tu proyecto?

En cuanto a seguridad, elegí la version de prueba de Firebase, por lo que no es tan compleja, pero no significa que no sea segura. Además, se validan los datos antes de almacenarlos (por ejemplo, asegurándose de que la cantidad y el precio sean números válidos) y se evitan duplicados con precios inconsistentes. El token de Telegram también se protege mediante variables de entorno.

- ¿Qué normativas (e.g., GDPR) podrían afectar el uso de tu software y cómo las has tenido en cuenta? Si no implementaste medidas de seguridad, ¿qué riesgos potenciales identificas y cómo los abordarías en el futuro?

El bot no maneja datos personales. Los riesgos incluyen acceso no autorizado a los datos o manipulación de inventario. Para abordarlos, se podrían añadir autenticación de usuarios, encriptación de datos sensibles y auditorías de seguridad. También sería útil implementar un sistema de logs para rastrear cambios y detectar actividades sospechosas y su proveniencia.

### Implicación de las THD en negocio y planta (2e):
- ¿Qué impacto tendría tu software en un entorno de negocio o en una planta industrial?

El bot de gestión de inventarios tendría un impacto positivo al automatizar y simplificar el control de stock, reduciendo errores humanos y ahorrando tiempo. En una planta industrial, permitiría un seguimiento en tiempo real de materiales y productos, mejorando la eficiencia operativa y reduciendo costos por desabastecimiento o exceso de inventario.

- ¿Cómo crees que tu solución podría mejorar procesos operativos o la toma de decisiones? Si tu proyecto no aplica directamente a negocio o planta, ¿qué otros entornos podrían beneficiarse?

El bot mejora los procesos operativos al centralizar y agilizar la gestión de inventarios, permitiendo a los usuarios agregar, consultar y eliminar productos de manera rápida y sencilla. Esto facilita la toma de decisiones al proporcionar datos actualizados y precisos sobre el stock disponible, ayudando a optimizar compras y producción.

### Mejoras en IT y OT (2f):
- ¿Cómo puede tu software facilitar la integración entre entornos IT y OT?

El bot de gestión de inventarios puede actuar como un puente entre IT y OT al permitir que los datos de inventario (OT) estén disponibles en tiempo real para sistemas de gestión empresarial (IT). Esto facilita la toma de decisiones basada en datos actualizados, mejorando la coordinación entre la planta de producción y la gestión administrativa.

- ¿Qué procesos específicos podrían beneficiarse de tu solución en términos de automatización o eficiencia? Si no aplica a IT u OT, ¿cómo podrías adaptarlo para mejorar procesos tecnológicos concretos?

Los procesos que podrían beneficiarse incluyen:

- Gestión de inventarios: Automatización del registro y seguimiento de materiales.

- Compras: Optimización de pedidos basada en niveles de stock.

- Producción: Reducción de tiempos de inactividad por falta de materiales.

- Auditorías: Simplificación de revisiones de inventario.

### Tecnologías Habilitadoras Digitales (2g):
- ¿Qué tecnologías habilitadoras digitales (THD) has utilizado o podrías integrar en tu proyecto?

En el proyecto se utiliza Firestore (base de datos en la nube) y la API de Telegram para la interacción con usuarios. En el futuro, se podrían integrar tecnologías como IA/ML para predecir demandas de inventario, IoT para conectar sensores de almacén, o blockchain para garantizar la trazabilidad de los productos.

- ¿Cómo mejoran estas tecnologías la funcionalidad o el alcance de tu software? Si no has utilizado THD, ¿cómo podrías implementarlas para enriquecer tu solución?

    - Firestore: Permite almacenar y acceder a datos en tiempo real, mejorando la eficiencia y escalabilidad.

    - API de Telegram: Facilita la interacción con usuarios de manera sencilla y accesible desde cualquier dispositivo.

    - IA/ML: Podría predecir tendencias de inventario, optimizando compras y reduciendo costos.

    - IoT: Permitiría monitorear automáticamente niveles de stock en almacenes.