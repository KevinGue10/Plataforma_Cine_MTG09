from flask import Flask,render_template
import sqlite3
from sqlite3 import Error
from db import get_db,close_db

app=Flask(__name__)

@app.route('/')
def index():
    db=get_db()
    snm=['','','','','']
    nm=['','','','','']
    for i in range (5):
        print(i)
        a=str(i+1)
        snm[i]=db.execute('Select name from Gpeliculas where ID='+a).fetchone()
    print(snm)
#    for i in range (5):
 #       x = snm[i].split("('")
  #      nm[i]=x[1].split("',)")

    print(nm)
    return render_template('Pagina_inicial.html',nm=snm)

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
    db=get_db()
    Datos=db.execute('Select * from Gpeliculas where ID=1').fetchone()
    print(Datos)
    return render_template('Pest_Pelicula1.html',Datos=Datos)

@app.route('/Pelicula2/')
def peli2():
    db=get_db()
    Datos=db.execute('Select * from Gpeliculas where ID=2').fetchone()
    print(Datos)
    ruta="{{url_for('static',filename='/image/Admin/Principales en cartelera/P2/Poster.jpg')}}"
    return render_template('Pest_Pelicula1.html',Datos=Datos, ruta=ruta)

@app.route('/Pelicula3/')
def peli3():
    db=get_db()
    Datos=db.execute('Select * from Gpeliculas where ID=3').fetchone()
    print(Datos)
    return render_template('Pest_Pelicula1.html',Datos=Datos)

@app.route('/Pelicula4/')
def peli4():
    db=get_db()
    Datos=db.execute('Select * from Gpeliculas where ID=4').fetchone()
    print(Datos)
    return render_template('Pest_Pelicula1.html',Datos=Datos)

@app.route('/Pelicula5/')
def peli5():
    db=get_db()
    Datos=db.execute('Select * from Gpeliculas where ID=3').fetchone()
    print(Datos)
    return render_template('Pest_Pelicula1.html',Datos=Datos)   
   
    
