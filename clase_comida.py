import pygame 
from colores import *
from variables import *
import random 


class Comida:
    def __init__(self) -> None:
        """metodo construcctor"""
        self.posicion_comida = (0,0)
        self.posicion_random()
        
    def posicion_random(self):
        """LE CREA UNA POSICION RANDOM A LA MANZANA"""
        self.posicion_comida = (random.randrange(40,ALTO_VENTANA-40,20) , random.randrange(40,ALTO_VENTANA-40,20))
    
    
    def dibujar_comida(self,ventana): 
        """DIBUJO LA POSICION DE LA MANZANA"""
        pygame.draw.rect(ventana, RED1, [self.posicion_comida[0],self.posicion_comida[1] , ANCHO_COMIDA , ALTO_COMIDA])
        
        