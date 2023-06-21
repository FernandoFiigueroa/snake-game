import pygame 
from colores import *
from variables import *
import random


class Bloque:
    def __init__(self) -> None:
        """inicio un constructor"""
        self.bloque_posicion = (0,0)
        self.posicion_random()
    
    def posicion_random(self):
        """ Creo una lista de tuplas de la posicion de los bloques"""
        self.bloque_posicion = [(random.randrange(40,ALTO_VENTANA,20), (random.randrange(40,ALTO_VENTANA,20))) for i in range(10)]

    
    def dibujar_bloque(self,ventana):
        """Funcion que me dibuja a los bloques"""
        for i, value in enumerate(self.bloque_posicion):
            pygame.draw.rect(ventana, BLACK, [value[0], value[1], ANCHO_BLOQUES, ALTO_BLOQUES]) #Value [0] = valor en x, Value [1] = valor en Y

