from inventario import InventarioClinica
from medicamento import Medicamento

inventario = InventarioClinica()

while True:
    print("""
    ===== INVENTARIO CLÍNICA =====
    1. Agregar medicamento
    2. Eliminar medicamento
    3. Mostrar inventario
    4. Salir
    """)

    opcion = input("Opción: ")

    if opcion == "1":
        id_ = int(input("ID: "))
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        inventario.agregar(Medicamento(id_, nombre, categoria, cantidad, precio))

    elif opcion == "2":
        id_ = int(input("ID a eliminar: "))
        inventario.eliminar(id_)

    elif opcion == "3":
        inventario.mostrar()

    elif opcion == "4":
        break
