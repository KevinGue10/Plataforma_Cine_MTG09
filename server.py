from flask import Flask,render_template,redirect,request,url_for, session,flash
import os
import sqlite3
from form import Inicio,Registro
from sqlite3 import Error
from db import get_db,close_db
from quer import nomb
#from crypt import methods
from distutils.log import debug, error
from email import message
import email
#import utils
from email.message import EmailMessage
import smtplib
app=Flask(__name__)
app.secret_key=os.urandom(30)



@app.route("/home")
@app.route("/index")
@app.route('/')
def index():
    db=get_db()
    nm=nomb(db)
    return render_template('Pagina_inicial.html',nm=nm)

@app.route('/Cartelera/')
def cartelera():
    return render_template('Cartelera.html')

@app.route('/Inises/')
def inises():
    form = Inicio()
    return render_template('Inicio_sesion.html', form=form)
    

@app.route('/Registro/')
def regis():
    frm = Registro()
    return render_template('Registro.html', frm=frm)

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
    nm=nomb(db)
    Datos=db.execute('Select * from Gpeliculas where ID=1').fetchone()
    print(Datos)
    
    return render_template('rutas.html',Datos=Datos,p=1,nm=nm)

@app.route('/Pelicula2/')
def peli2():
    db=get_db()
    nm=nomb(db)
    Datos=db.execute('Select * from Gpeliculas where ID=2').fetchone()
    print(Datos)
    return render_template('rutas.html',Datos=Datos,p=2, nm=nm)

@app.route('/Pelicula3/')
def peli3():
    db=get_db()
    nm=nomb(db)
    Datos=db.execute('Select * from Gpeliculas where ID=3').fetchone()
    print(Datos)
    return render_template('rutas.html',Datos=Datos,p=3, nm=nm)

@app.route('/Pelicula4/')
def peli4():
    db=get_db()
    nm=nomb(db)
    Datos=db.execute('Select * from Gpeliculas where ID=4').fetchone()
    print(Datos)
    return render_template('rutas.html',Datos=Datos,p=4, nm=nm)

@app.route('/Pelicula5/')
def peli5():
    db=get_db()
    Datos=db.execute('Select * from Gpeliculas where ID=5').fetchone()
    print(Datos)
    return render_template('Pest_Pelicula1.html',Datos=Datos)   

@app.route('/Tick1/')
def tiquete1():
     return render_template('rutas2.html',p=1) 
     
       
@app.route('/Registro/',methods=['POST'])
def Usuarios():      
 frm = Registro()
   
 username = frm.nombre.data
 rol= 1
 password = frm.contraseña.data
            # Conecta a la BD
 with sqlite3.connect("Pcine.db") as con:
                cursor = con.cursor()  # Manipular la BD
                # Prepara la sentencia SQL a ejecutar
                cursor.execute("INSERT INTO usuario (rol,nombre, password) VALUES(?,?,?)", [
                            rol,username, password])
                # Ejecuta la sentencia SQL
                con.commit()
                return redirect("/")
 
@app.route('/Inicio_sesion',methods=['POST'])
def inisesion():    
 frm = Inicio()
 username = frm.usuario.data
 password = frm.contraseña.data 
 with sqlite3.connect("Pcine.db") as con:
  con.row_factory = sqlite3.Row
  cursor = con.cursor()
  cursor.execute("SELECT * FROM usuario WHERE nombre = ? AND password = ?", [username, password])

            # cursor.execute(f"SELECT username FROM usuario WHERE nombre = '{username}' AND password = '{pass_enc}'")
 row = cursor.fetchone()
 if row:
                # Se crea la sesión
    session['usuario'] = username
    session['rol'] = row["rol"]
    if session["rol"] == "1":
      return redirect("/")
    elif session["rol"] == "2":
      return redirect("/")
    elif session["rol"] == "3":
      return redirect("/")
    else:
      flash(message="Usuario no válido") 
       
 return redirect("/")
app.run(debug=True)

    
