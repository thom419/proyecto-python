#creación de un programa de inventario en Python
# el programa permite gestionar un inventario de productos con funcionalidades para registrar, actualizar, eliminar y buscar
import sqlite3
# creación de la base de datos y la tabla de productos
def conectar_db():
    return sqlite3.connect("inventario.db")

def crear_tabla():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    """)
    conn.commit()
    conn.close()

def registrar_producto():
    print("\nRegistrar nuevo producto")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    categoria = input("Categoría: ")

    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, descripcion, cantidad, precio, categoria))
    conn.commit()
    conn.close()
    print("Producto registrado")

def visualizar_productos():
    print("\nLista de productos:")
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()

    if productos:
        for p in productos:
            print(f"ID: {p[0]} | Nombre: {p[1]} | Cantidad: {p[3]} | Precio: {p[4]} | Categoría: {p[5]}")
    else:
        print("No hay productos registrados")

def actualizar_producto_por_id():
    print("\nActualizar producto")
    id_producto = input("Ingresá el ID del producto: ")

    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()

    if producto:
        print("Dejá vacío si no querés cambiar el dato.")
        nombre = input(f"Nuevo nombre ({producto[1]}): ") or producto[1]
        descripcion = input(f"Nueva descripción ({producto[2]}): ") or producto[2]
        cantidad = input(f"Nueva cantidad ({producto[3]}): ") or producto[3]
        precio = input(f"Nuevo precio ({producto[4]}): ") or producto[4]
        categoria = input(f"Nueva categoría ({producto[5]}): ") or producto[5]

        cursor.execute("""
            UPDATE productos
            SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
            WHERE id = ?
        """, (nombre, descripcion, int(cantidad), float(precio), categoria, id_producto))
        conn.commit()
        print("Producto actualizado")
    else:
        print("No se encontró el producto")
    conn.close()

def eliminar_producto_por_id():
    print("\nEliminar producto")
    id_producto = input("Ingresá el ID del producto a eliminar: ")

    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()

    if producto:
        confirmacion = input(f"¿Seguro que querés eliminar '{producto[1]}'? (s/n): ").lower()
        if confirmacion == "s":
            cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
            conn.commit()
            print("Producto eliminado")
        else:
            print("Operación cancelada")
    else:
        print("No se encontró el producto")
    conn.close()

def buscar_producto_por_id():
    print("\nBuscar producto por ID")
    id_producto = input("Ingresá el ID: ")

    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()
    conn.close()

    if producto:
        print(f"ID: {producto[0]} | Nombre: {producto[1]} | Descripción: {producto[2]} | Cantidad: {producto[3]} | Precio: {producto[4]} | Categoría: {producto[5]}")
    else:
        print("No se encontró el producto")
#reporte de productos con bajo stock
def reportar_bajo_stock(limite):
    print(f"\nProductos con stock menor o igual a {limite}:")
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    productos = cursor.fetchall()
    conn.close()

    if productos:
        for p in productos:
            print(f"ID: {p[0]} | Nombre: {p[1]} | Cantidad: {p[3]} | Precio: {p[4]} | Categoría: {p[5]}")
    else:
        print("No hay productos con bajo stock")
# menú de opciones para interactuar con el usuario
def menu():
    print("\nMenú:")
    print("1. Registrar producto")
    print("2. Visualizar productos")
    print("3. Actualizar producto por ID")
    print("4. Eliminar producto por ID")
    print("5. Buscar producto por ID")
    print("6. Reporte de bajo stock")
    print("7. Salir")
#menu de opciones para interactuar con el usuario
def iniciar_aplicacion():
    crear_tabla()
    while True:
        menu()
        try:
            opcion = int(input("Elegí una opción: "))
            if opcion == 1:
                registrar_producto()
            elif opcion == 2:
                visualizar_productos()
            elif opcion == 3:
                actualizar_producto_por_id()
            elif opcion == 4:
                eliminar_producto_por_id()
            elif opcion == 5:
                buscar_producto_por_id()
            elif opcion == 6:
                limite = int(input("Ingresá el límite de stock: "))
                reportar_bajo_stock(limite)
            elif opcion == 7:
                print("Fin del programa")
                break
            else:
                print("Opción inválida")
        except ValueError:
            print("Ingresá un número válido")

if __name__ == "__main__":
    iniciar_aplicacion()

