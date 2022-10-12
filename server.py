<<<<<<< HEAD
from crypt import methods
from distutils.log import debug, error
from email import message
import email
from flask import Flask,render_template,redirect,request,url_for, session,flash
import utils
from email.message import EmailMessage
import smtplib
import os

app=Flask(__name__)
app.secret_key=os.urandom(30)

nombre1='Spiderman Sin camino a casa'
=======
from flask import Flask,render_template
import os
import sqlite3
from sqlite3 import Error
from db import get_db,close_db
from quer import nomb

app=Flask(__name__)

>>>>>>> kevin
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
<<<<<<< HEAD
    return render_template('Pest_Pelicula1.html')
@app.route('/')
def registrar():    
    return render_template('Registro.html')
@app.route('/Registro/',methods=('GET','POST'))
def register():    
    try:
        if request.method== 'POST':
            usuario= request.form['nombres']
            password =request.form['contraseña']
            email = request.form['correo']
            error=None

        if not utils.utils.isUsernameValid(usuario):
                error="El nombre debe ser alfanumerico"
                flash(error)
                return render_template('Registro.html')
        if not utils.utils.isEmailValid(email):
                error="El correo no es valido"
                flash(error)
                return render_template('Registro.html')  
        if not utils.utils.isPasswordValid(password):
                error="La contraseña debe tener una minuscula,una mayuscula,un numero y minimo 8 caracteres"
                flash(error)
                return render_template('Registro.html')  
        credentials={
           'user':'alejandradv@uninorte.edu.co',
           'password':'xxxxxx'     
        }                    
        send_email(credentials=credentials, receiver =email, 
        subject='Activa tu cuenta', 
        message='Bienvenido activa tu cuenta atraves de este link')
        flash('Revisa tu correo para activar tu cuenta')
        return render_template('Inicio_sesion.html')  
      
    except:
        return f'Ocurrio un error'  

def send_email(credentials, receiver, subject, messade):
    email=EmailMessage()
    email["From"]=credentials["user"]
    email["To"]=receiver
    email["Subject"]= subject
    email.set_content(message)

    smtp=smtplib.SMTP("smtp-mail.outlook.com",port=587)
    smtp.starttls()
    smtp.login(credentials['user'],credentials['password'])
    smtp.sendmail(credentials['user'],receiver,email.as_string())
    smtp.quit()
=======
    
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

>>>>>>> kevin
    
