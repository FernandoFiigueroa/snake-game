import sqlite3
import pygame
from variables import *
from colores import *
import sys


#creo una tabla con los nombre y score de los ususarios
img_datos = pygame.image.load("snake_game/imagenes/fondo_puntu.png")
img_datos = pygame.transform.scale(img_datos,(ANCHO_VENTANA+50,ALTO_VENTANA))

img_preguntar_puntu = pygame.image.load("snake_game/imagenes/menu_puntuacion.png")
img_preguntar_puntu = pygame.transform.scale(img_preguntar_puntu,(ANCHO_VENTANA+50,ALTO_VENTANA))

with sqlite3.connect("datos.db") as conexion:
    
							"""Creo una tabla con los datos del usuario """
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

#conexion = Objeto


def insertar(nombre:str,score:int):
		"""Inserto los datos del usuario a la tabla(sql)"""
		try:	
								conexion.execute("INSERT INTO puntuaciones(nombre,score) VALUES (?,?)",(nombre,score))
								print("Se creo la tabla con exito")
								conexion.commit()# Actualiza los datos realmente en la tabla
		except:
								print("Error en la ejecucion")


def datos(ventana):
	"""Le pregunto al usuario si quiere salir del juego o si quiere saber las puntuaciones de los jugadores"""
	print(type(ventana))
	correr =True
	while correr:
		lista_eventos = pygame.event.get()
		ventana.blit(img_preguntar_puntu,img_preguntar_puntu.get_rect()) 
		for evento in lista_eventos:
						if evento.type == pygame.QUIT:
									pygame.quit()      
						if evento.type == pygame.KEYDOWN:
							if evento.key == pygame.K_a:
									correr  = False
							if evento.key == pygame.K_y:
										pygame.quit
										sys.exit()
							if evento.key == pygame.K_c:
										menor_puntuacion(ventana)
							if evento.key == pygame.K_x:
										mayor_puntuacion(ventana)			
		pygame.display.flip()
     
     
def mayor_puntuacion(ventana):
	"""La funcion me muestra el nombre y el score del jugador que mayor score tiene  """
	correr = True
	cursor = conexion.execute("SELECT * FROM puntuaciones ORDER BY score") #Forma ascendente	
	while correr:
		lista_eventos = pygame.event.get()
		ventana.blit(img_datos,img_datos.get_rect()) 
		for fila in cursor:
			nombre_usu = fila[1]
			score_usuario = fila[2]
		for evento in lista_eventos:	
					"""VERIFICO SI EL USUARIO QUIERE SEGUIR JUGANDO O SALIR"""
					if evento.type == pygame.QUIT:
							pygame.quit()      
					if evento.type == pygame.KEYDOWN:
							if evento.key == pygame.K_f:
											correr  = False
							if evento.key == pygame.K_y:
										pygame.quit
										sys.exit()
		mostrar_datos(ventana,nombre_usu,score_usuario)
		pygame.display.flip()


def menor_puntuacion(ventana):
	"""La funcion me muestra el nombre y el score del jugador que MENOR score tiene  """
	cursor = conexion.execute("SELECT * FROM puntuaciones ORDER BY score DESC") #Forma ascendente
	correr = True	
	while correr:
		lista_eventos = pygame.event.get()
		ventana.blit(img_datos,img_datos.get_rect()) 
		for fila in cursor:
			nombre_usu = fila[1]
			score_usuario = fila[2]
		for evento in lista_eventos:	
					"""VERIFICO SI EL USUARIO QUIERE SEGUIR JUGANDO O SALIR"""
					if evento.type == pygame.QUIT:
							pygame.quit()      
					if evento.type == pygame.KEYDOWN:
							if evento.key == pygame.K_f:
										correr  = False
							if evento.key == pygame.K_y:
										pygame.quit
										sys.exit()
		mostrar_datos(ventana,nombre_usu,score_usuario)
		pygame.display.flip()



def mostrar_datos(ventana,nombre_usu:str, score_usuario:int):
    
		font_pausa = pygame.font.SysFont("Oswald", 60) 
  
		nombre = font_pausa.render("{0}".format(nombre_usu),True,WHITE)
		ventana.blit(nombre,(ANCHO_VENTANA-500,ALTO_VENTANA-300 ))
  
		score = font_pausa.render("{0}".format(score_usuario),True,WHITE)
		ventana.blit(score,(ANCHO_VENTANA-180, ALTO_VENTANA-300))

