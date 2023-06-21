import pygame
from variables import *


def crear_jugar():
    imagen_jugar = pygame.image.load("snake_game/imagenes/jugar.png")
    imagen_jugar = pygame.transform.scale(imagen_jugar,(ANCHO_JUGAR, ALTO_JUGAR))
    rect_boton = imagen_jugar.get_rect()
    dic_puntaje = {}
    dic_puntaje["superficie"] = imagen_jugar
    dic_puntaje["rectangulo"] = rect_boton
    return dic_puntaje

   
class ButtonJugar: 
    def __init__(self) -> None:
        """Creo un constructor"""
        self.diccionario = crear_jugar()
        self.imagen = self.diccionario["superficie"]
        self.rect_boton = self.diccionario["rectangulo"]
        self.rect_boton.x = POS_X
        self.rect_boton.y = POS_Y_JUGAR
        self.jugar = 0
       
    
    def draw(self,ventana_principal):
            """Dibujo en pantalla mi imagen"""
            ventana_principal.blit(self.imagen, self.rect_boton)   
        
    def recibir_lista(self,lista_eventos):
            
            """Si el usuario oprime sobre cualquiero parte de la superficie de la imgagen la funcion devuelve un 1 """
            
            if( lista_eventos[0] > self.rect_boton[0] and lista_eventos[0]< (self.rect_boton[0]+self.rect_boton[2])):
                    if( lista_eventos[1]> self.rect_boton[1] and lista_eventos[1]< (self.rect_boton[1]+self.rect_boton[3])):
                        self.jugar = 1
            return self.jugar
        
