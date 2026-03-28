class Medicamento:
    def __init__(self, id_medicamento, nombre, categoria, cantidad, precio):
        self.id = id_medicamento
        self.nombre = nombre
        self.categoria = categoria
        self.cantidad = cantidad
        self.precio = precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio
