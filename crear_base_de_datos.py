import sqlite3
from clase_nombre import Datos

datos = Datos()

""" creo una tabla con los nombre y score de los ususarios"""
with sqlite3.connect("datos.db") as conexion:
					try:
						sentencia = ''' create  table puntuaciones
						(
						id integer primary key autoincrement,
						nombre text,
						score INTEGER
						)
						'''
						conexion.execute(sentencia)
						print("Se creo la tabla puntuaciones")                       
					except sqlite3.OperationalError:
						print("La tabla puntuaciones ya existe")


def insertar_datos_en_BD(score,nombre):   
    
	""" inserto a la tabla el nombre y el score de los usuarios"""
	try:	
					conexion.execute("INSERT INTO puntuaciones(nombre,score) VALUES (?,?)",(nombre,score))
					conexion.commit()# Actualiza los datos realmente en la tabla
	except:
					print("Error en la ejecucion")
     
def datos_ordenados():
    
	""" ordeno la tabla de manera descendente"""
 
	cursor = conexion.execute("SELECT * FROM puntuaciones ORDER BY score DESC") #Forma descendente
	for fila in cursor:
		return fila
  
puntuaciones = datos_ordenados()