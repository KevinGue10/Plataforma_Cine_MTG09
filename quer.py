import sqlite3
from sqlite3 import Error
from flask import g
from db import get_db,close_db

def nomb(dba):
    db=dba
    snm=['','','','','','','','','','']
    for i in range (5):
        snm[i]=db.execute('Select name from Gpeliculas where ID= ?',[i+1]).fetchone()
    print(snm)
  #  snm= "".join(snm)
  # for i in range (5):
  #       x = snm[i].split("('")
  #      nm[i]=x[1].split("',)")

    return snm

def mdato(p):
    db=get_db()
    snm=db.execute('Select * from Gpeliculas where ID= ?',p).fetchone()
    return 'cambio'
    
def agp(nm,nombre,original,genero,duracion,resumen,reparto,director):
    db=get_db()
    db.execute("UPDATE Gpeliculas SET name ='"+nombre+"' , Original = '"+original+"', Generos = "+
    genero+", Duracion = '"+duracion+"', Resumen = '"+resumen+"', Reparto = '"+reparto+"', Director= '"+director+"' WHERE ID ="+nm )