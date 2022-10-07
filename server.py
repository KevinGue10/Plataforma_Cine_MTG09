from flask import Flask,render_template
app=Flask(__name__)
nombre1='Spiderman Sin camino a casa'
@app.route('/')
def index():
    return render_template('Pagina_inicial.html')

@app.route('/Cartelera/')
def cartelera():
     return render_template('Cartelera.html')

@app.route('/Pelicula1/')
def peli1():
    return render_template('Pest_Pelicula1.html')

@app.route('/Agregarpelicula/')
def Agpelicula():
    return render_template('agregarpelicula.html')

@app.route('/Gestionarpelicula/')
def Gpeliculas():
    return render_template('Gestionarpelicula.html')