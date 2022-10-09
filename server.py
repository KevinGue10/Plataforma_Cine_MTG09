from flask import Flask,render_template


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('Pagina_inicial.html')

@app.route('/Cartelera/')
def cartelera():
    return render_template('Cartelera.html')

@app.route('/Inises/')
def inises():
    return render_template('Inicio_sesion.html')

@app.route('/Registro/')
def regis():
    return render_template('Registro.html')

@app.route('/Opinion/')
def opinion():
    return render_template('opinion.html')

@app.route('/Agregarpelicula/')
def Agpelicula():
    return render_template('agregarpelicula.html')

@app.route('/Gestionarpelicula/')
def Gpeliculas():
    return render_template('Gestionarpelicula.html')

@app.route('/Gestinarusuarios/')
def Gusuar():
    return render_template('gestinarusuarios.html')

@app.route('/Pelicula1/')
def peli1():
    return render_template('Pest_Pelicula1.html')

@app.route('/Pelicula2/')
def peli2():
    return render_template('Pest_Pelicula2.html')

@app.route('/Pelicula3/')
def peli3():
    return render_template('Pest_Pelicula3.html')    

