import pygame 
from variables import *
from colores import *
from funciones import main
from funciones import draw_ingreso_nombre
from jugar import ButtonJugar
from clase_nombre import Datos



datos = Datos()
jugar = ButtonJugar()

pygame.init()
ventana = pygame.display.set_mode((ALTO_VENTANA,ANCHO_VENTANA))
pygame.display.set_caption("Snake Game")#Titulo del juego


img_fondo = pygame.image.load("snake_game/imagenes/background.jpg")
img_fondo = pygame.transform.scale(img_fondo,(ANCHO_VENTANA, ALTO_VENTANA))

img_menu = pygame.image.load("snake_game/imagenes/background_inicio.jpg")
img_menu = pygame.transform.scale(img_menu,(ALTO_MENU,ANCHO_VENTANA ))


clock = pygame.time.Clock()

correr = True

while correr:

    if JUGANDO == 0:
        """ PANTALLA DE INICIO """
        draw_ingreso_nombre(ventana,img_menu,datos.devolder_nombre())  
        lista_eventos = pygame.event.get()
        jugar.draw(ventana)
        pygame.display.flip()
        for evento in lista_eventos:
                        if evento.type == pygame.QUIT:
                                        correr = False
                        if evento.type == pygame.KEYDOWN:
                                nombre_ingresado = datos.nombre_a_ingresar(evento)
                        if evento.type == pygame.MOUSEBUTTONDOWN:
                                lista_click = list(evento.pos)
                                if len(datos.devolder_nombre()) > 1:
                                        JUGANDO = jugar.recibir_lista(lista_click)
                                else:
                                        JUGANDO = 0

    if JUGANDO == 1:
        """llamo a la funcion main"""
        
        JUGANDO =  main(ventana,clock,img_fondo)             
                               
pygame.display.flip()

