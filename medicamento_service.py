from conexion.conexion import get_connection

def obtener_medicamentos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM medicamentos")
    data = cursor.fetchall()
    conn.close()
    return data


def insertar_medicamento(nombre, categoria, cantidad, precio):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO medicamentos (nombre, categoria, cantidad, precio) VALUES (%s, %s, %s, %s)",
        (nombre, categoria, cantidad, precio)
    )
    conn.commit()
    conn.close()


def obtener_medicamento(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM medicamentos WHERE id=%s", (id,))
    data = cursor.fetchone()
    conn.close()
    return data


def actualizar_medicamento(id, nombre, categoria, cantidad, precio):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE medicamentos SET nombre=%s, categoria=%s, cantidad=%s, precio=%s WHERE id=%s",
        (nombre, categoria, cantidad, precio, id)
    )
    conn.commit()
    conn.close()


def eliminar_medicamento(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM medicamentos WHERE id=%s", (id,))
    conn.commit()
    conn.close()