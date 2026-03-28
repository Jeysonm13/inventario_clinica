import sqlite3

class Database:
    def __init__(self, db_name="inventario_clinica.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicamentos (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            categoria TEXT,
            cantidad INTEGER,
            precio REAL
        )
        """)
        self.conn.commit()
