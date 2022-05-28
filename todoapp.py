#importar librerias de Flask y tkinter
from tkinter import SW
from flask import Flask,  abort, flash, redirect, request,render_template, url_for

#Iniciar variable de aplicacion 
app= Flask(__name__, template_folder='templates')

#Definición de arreglo para ingresar los datos
tareasPendientes = []

#Primer controlador - decorador para definir la ruta raíz e index 
@app.route('/' )
#Función principal que llamará a la página HTML y encapsula la variable de nuestro arreglo
def principal():
    return render_template('pagina1.html', tareasLista = tareasPendientes)

#segundo controlador el cuál almacenara los elementos que ingresemos por el formulario HTML
@app.route('/enviar',  methods=['GET','POST'])
#Función enviar la cuál podrá almacenar los datos ingresados por medio del formulario dentro de nuestro arreglo
def enviar():
    if(request.method == "POST"):
        tareas = request.form['tarea']
        correos = request.form['correo']
        prioridades = request.form['prioridad']
        tareasPendientes.append({'tarea': tareas, 'correo': correos, 'prioridad': prioridades })
        return redirect(url_for('principal'))

#Tercer controlador el cuál borrara la lista de tareas
@app.route('/borrar', methods=["GET","POST"])
#Función borrar la cuál limpiara todos los elementos que se encuentren almacenados dentro de nuestro arreglo
def borrar():
    if(request.method == "POST"):
        tareasPendientes.clear()
        return redirect(url_for('principal'))

# main del programa 
if __name__ == '__main__':
    #debug = true, para reiniciar automaticamente el servidor, tiempo de desarrollo 
    app.run(debug=True)