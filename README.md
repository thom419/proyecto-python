# Inventario (entrega_final_curso.py)

Descripción
-----------
Aplicación de consola en Python para gestionar un inventario simple usando SQLite. Permite registrar, listar, actualizar, buscar y eliminar productos, además de generar un reporte de productos con bajo stock.

Características
---------------
- Crea automáticamente la base de datos SQLite (`inventario.db`) y la tabla `productos` si no existen.
- Registrar nuevos productos con: nombre, descripción, cantidad, precio y categoría.
- Visualizar todos los productos registrados.
- Actualizar un producto por su ID (permite mantener valores actuales dejando el campo vacío).
- Eliminar un producto por su ID (con confirmación).
- Buscar detalles de un producto por su ID.
- Reporte de productos con stock menor o igual a un límite proporcionado.

Requisitos
----------
- Python 3.6 o superior.
- No requiere paquetes externos; usa la librería estándar `sqlite3`.

Instalación y uso
-----------------
1. Clona o descarga el repositorio:
   ```
   git clone https://github.com/thom419/proyecto-python
   ```

2. Sitúate en la carpeta del proyecto y ejecuta:
   ```
   python entrega_final_curso.py
   ```

3. Usa el menú en la consola para interactuar:
   - 1. Registrar producto
   - 2. Visualizar productos
   - 3. Actualizar producto por ID
   - 4. Eliminar producto por ID
   - 5. Buscar producto por ID
   - 6. Reporte de bajo stock
   - 7. Salir

Detalles técnicos
-----------------
- Archivo de base de datos: `inventario.db` (se crea en la misma carpeta al ejecutar el script).
- Tabla: `productos` con columnas:
  - `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
  - `nombre` (TEXT NOT NULL)
  - `descripcion` (TEXT)
  - `cantidad` (INTEGER NOT NULL)
  - `precio` (REAL NOT NULL)
  - `categoria` (TEXT)

Ejemplos rápidos
----------------
- Registrar: elige opción `1` y proporciona `Nombre`, `Descripción`, `Cantidad`, `Precio` y `Categoría`.
- Visualizar: elige opción `2` para listar todos los productos.
- Actualizar: elige opción `3`, ingresa el ID; deja campos en blanco para no modificar un valor.
- Reporte de bajo stock: opción `6` e ingresa el límite (por ejemplo `5`) para ver productos con `cantidad <= 5`.

Limitaciones y mejoras sugeridas
-------------------------------
- Validación de entradas: actualmente la conversión a int/float puede lanzar excepciones si el usuario ingresa texto no numérico. Añadir validaciones y manejo de errores.
- Manejo de errores de la base de datos con bloques `try/except`.
- Búsqueda y filtrado: añadir búsqueda por nombre o categoría, y paginación para listados grandes.
- Importación/Exportación: añadir exportación a CSV y posibilidad de importar productos.
- Interfaz: considerar una interfaz gráfica (Tkinter) o una API REST para acceso remoto.
- Concurrencia: si habrá acceso multiusuario, añadir control de concurrencia y/o migrar a un motor de BD servidor.

Contribuciones
--------------
Si quieres mejorar el proyecto:
- Abre un issue describiendo el cambio o bug.
- Envía un pull request con pruebas y documentación de los cambios.

Contacto
-------
Para dudas o sugerencias, crea un issue en el repositorio.
