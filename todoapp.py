#importamos la libreía Markupsafe
from markupsafe import escape

#importar libreria de Flask
from tkinter import SW
from flask import Flask,  abort, flash, redirect, request,render_template, url_for

#Iniciar variable de aplicacion 
app= Flask(__name__, template_folder='templates')

#Definición de arreglo para ingresar los datos
tareasPendientes = []

#decorador para definir la ruta raíz que llevará a nuestro html página1
@app.route('/' )
def principal():
    return render_template('pagina1.html')


# main del programa 
if __name__ == '__main__':
    #debug = true, para reiniciar automaticamente el servidor , tiemo de desarrollo 
    app.run(debug=True)