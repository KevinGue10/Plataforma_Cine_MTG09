from flask import Flask,render_template,redirect,request,url_for, session,flash
import os
import sqlite3
from form import Inicio,Registro
from sqlite3 import Error
from db import get_db,close_db
from quer import nomb,gene
from form_pel import FormPel
from werkzeug.utils import secure_filename
from carpetas import rutc
from forms import Opinion
from Forms_tick import Ticket

app=Flask(__name__)

app.secret_key=os.urandom(24)

@app.route("/home")
@app.route("/index")
@app.route('/')
def index():
    db=get_db()
    Datos=nomb(db)
    desc=db.execute('Select * from Gpeliculas where ID=1').fetchone()
    return render_template('Pagina_inicial.html',Datos=Datos,des=desc)

@app.route('/Cartelera/')
def cartelera():
    db=get_db()
    Datos=nomb(db)
    gen=gene(db)

    return render_template('Cartelera.html',Datos=Datos,gene=gen)

@app.route('/Inises/')
def inises():
    return render_template('Inicio_sesion.html')

@app.route('/Registro/')
def regis():
    return render_template('Registro.html')

@app.route('/Agregarpelicula<string:p>/', methods=['GET','POST'])
def Agpelicula(p):
    form=FormPel()
    db=get_db()
    Datos=db.execute('Select * from Gpeliculas where ID=?',p).fetchone()
    if (form.validate_on_submit()):
        name=request.form['titulo']
        original=request.form['original']
        genero=request.form['genero']
        duracion=request.form['duracion']
        resumen=request.form['resumen']
        reparto=request.form['reparto']
        director=request.form['director']
        numpel=p
        db.execute("UPDATE Gpeliculas SET name ='"+name+"' , Original = '"+original+"', Generos = '"+genero+"', Duracion = '"+duracion+
        "', Resumen = '"+resumen+"', Reparto = '"+reparto+"', Director= '"+director+"' WHERE ID ="+numpel)
        db.commit()
    return render_template('fmpel.html',form=form,p=int(p),Datos=Datos)

@app.route('/Gestionarpelicula/')
def Gpeliculas():
    db=get_db()
    Datos=nomb(db)
    return render_template('Gestionarpelicula.html',Datos=Datos)

@app.route('/Gestinarusuarios/')
def Gusuar():
    return render_template('gestinarusuarios.html')

@app.route('/Pelicula<string:p>/')
def peli1(p):
    
    db=get_db()
    nm=nomb(db)
    Datos=db.execute('Select * from Gpeliculas where ID=?',p).fetchone()
    nom=Datos[1]
    print(nom)
    cal=db.execute("Select calificacion from opinion where pelicula='"+nom+"'").fetchall()
    print(cal)
    r=int(p)
    return render_template('rutas.html',Datos=Datos,p=r,nm=nm)


@app.route('/Tick<string:p>/', methods=['GET','POST'])
def peliti1(p):  
    db=get_db()
    nm=nomb(db)
    total=0
    precio=0
    form = Ticket()
    Datos=db.execute('Select * from Gpeliculas where ID=?',p).fetchone()
    if (form.validate_on_submit()):
        funcion=request.form['funcion']
        cantidad=request.form['cantidad']
        if funcion=='Funcion Estandar':
            precio=10000
        elif funcion=='Funcion VIP':
            precio=16000
        print(cantidad)
        total=precio*int(cantidad)
        print(total)
    return render_template('rutas2.html',Datos=Datos,p=int(p),nm=nm,form=form,subtotal=total,precio=precio)

def all_file(file):
    file=file.split('.')
    if file[1] in AEX:
        return True
    return False

AEX=set(['png',"jpg","jpeg"])
@app.route('/upload<string:p>', methods=["POST"])
def upload(p):
    print("valor"+p)
    p=int(p)
    UB=rutc(p,app)

    filep=request.files["uploadFile"]
    fileb=request.files["uploadBFile"]
    filenamep=secure_filename(filep.filename)
    filenameb=secure_filename(fileb.filename)
    if filep and all_file(filenameb):
        print("permitido")
        filep.save(os.path.join(UB,filenamep))

    if fileb and all_file(filenameb):
        print("permitido")
        fileb.save(os.path.join(UB,filenameb))
    
    return redirect(url_for('Agpelicula',p=p))

def sql_insert_products(pelicula,calificacion,comentario,usuario):
    strsql="INSERT INTO opinion (pelicula,calificacion,comentario,usuario) VALUES('"+pelicula+"',"+calificacion+",'"+comentario+"','"+usuario+"');"
    con=get_db()
    cursorObj=con.cursor()
    cursorObj.execute(strsql)
    con.commit()
    con.close()

@app.route('/Opinion/', methods=['GET','POST'])
def nuevo():
    if request.method=="GET":
        form = Opinion()
        con = get_db()
        pelis=nomb(con)
        print(pelis)
        form.pelicula.choices = pelis      
        return render_template('opinion.html', form=form)
    
    if request.method=='POST':
        peli = request.form["pelicula"]
        cali = request.form["calificacion"]
        cant = request.form["comentario"]
        usua = request.form["usuario"]
        sql_insert_products(peli,cali,cant,usua)
        return "Comentario enviado"

