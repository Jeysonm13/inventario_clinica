from flask import Flask, render_template, request, redirect, url_for
from services.medicamento_service import *
from forms.medicamento_form import MedicamentoForm

app = Flask(__name__)

# LISTAR
@app.route('/')
def listar():
    medicamentos = obtener_medicamentos()
    return render_template('medicamentos/listar.html', medicamentos=medicamentos)


# CREAR
@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        form = MedicamentoForm(request.form)
        insertar_medicamento(form.nombre, form.categoria, form.cantidad, form.precio)
        return redirect(url_for('listar'))
    return render_template('medicamentos/crear.html')


# EDITAR
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    medicamento = obtener_medicamento(id)

    if request.method == 'POST':
        form = MedicamentoForm(request.form)
        actualizar_medicamento(id, form.nombre, form.categoria, form.cantidad, form.precio)
        return redirect(url_for('listar'))

    return render_template('medicamentos/editar.html', medicamento=medicamento)


# ELIMINAR
@app.route('/eliminar/<int:id>')
def eliminar(id):
    eliminar_medicamento(id)
    return redirect(url_for('listar'))


# PDF
from reportlab.platypus import SimpleDocTemplate, Table

@app.route('/reporte')
def reporte():
    medicamentos = obtener_medicamentos()

    data = [["ID", "Nombre", "Categoría", "Cantidad", "Precio"]]

    for m in medicamentos:
        data.append([m['id'], m['nombre'], m['categoria'], m['cantidad'], m['precio']])

    pdf = SimpleDocTemplate("reporte_medicamentos.pdf")
    tabla = Table(data)
    pdf.build([tabla])

    return "Reporte generado"


if __name__ == '__main__':
    app.run(debug=True)