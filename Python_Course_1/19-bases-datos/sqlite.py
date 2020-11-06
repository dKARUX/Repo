import sqlite3

# Conexión
conexion = sqlite3.connect("pruebas.db")

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255), 
    descripcion TEXT,
    precio int(255)
)""")

# Guardar cambios
conexion.commit()

# Insertar datos
"""
cursor.execute("INSERT INTO productos VALUES (null, 'Segundo producto', 'Descripción de mi producto', 550)")
conexion.commit()
"""

# Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

# Insertar muchos registros de golpe
productos = [
    ('Jabon', 'Limpieza', 15),
    ('Peluche', 'Acurrucarse', 1500),
    ('Inflable', 'Juguete para albercas', 200)
]

cursor.executemany(f"INSERT INTO productos VALUES (null, ?, ?, ?)", productos)
conexion.commit()

# Listar datos
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()

print("\nLa Lista de Tuplas creada a partir de la base de datos...\n")
print(productos)

# Recorrer la BD a traves de las Tuplas creadas usando bucle FOR
print("\nRecorriendo la Lista de Tuplas creada usando bucle FOR...\n")
for producto in productos:
    print(producto)

# Cerrar la conexión
conexion.close()