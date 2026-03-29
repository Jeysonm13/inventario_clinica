class MedicamentoForm:
    def __init__(self, form):
        self.nombre = form.get("nombre")
        self.categoria = form.get("categoria")
        self.cantidad = form.get("cantidad")
        self.precio = form.get("precio")