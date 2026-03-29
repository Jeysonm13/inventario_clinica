from medicamento import Medicamento
from conexion import Database

class InventarioClinica:
    def __init__(self):
        self.db = Database()
        self.medicamentos = {}
        self.cargar_datos()

    def cargar_datos(self):
        self.db.cursor.execute("SELECT * FROM medicamentos")
        for id_, nombre, categoria, cantidad, precio in self.db.cursor.fetchall():
            self.medicamentos[id_] = Medicamento(id_, nombre, categoria, cantidad, precio)

    def agregar(self, med):
        self.medicamentos[med.id] = med
        self.db.cursor.execute(
            "INSERT INTO medicamentos VALUES (?, ?, ?, ?, ?)",
            (med.id, med.nombre, med.categoria, med.cantidad, med.precio)
        )
        self.db.conn.commit()

    def eliminar(self, id_med):
        if id_med in self.medicamentos:
            del self.medicamentos[id_med]
            self.db.cursor.execute("DELETE FROM medicamentos WHERE id = ?", (id_med,))
            self.db.conn.commit()

    def mostrar(self):
        for m in self.medicamentos.values():
            print(f"{m.id} | {m.nombre} | {m.categoria} | {m.cantidad} | ${m.precio}")
