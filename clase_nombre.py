import pygame
from variables import * 
from colores import *

class Datos:
    def __init__(self) -> None:
        """creo un constructor"""
        self.nombre_ingresado = ' '
    
    def nombre_a_ingresar(self,evento):
            """ La funcion lo que haces es: gaurdar los datos que el usuario ingresa como nombre dentro de la variable nombre_ingresado y la retorna"""
            if evento.key == pygame.K_BACKSPACE:
                        """Si borra la ultima letra se guarda todo menos lo que borro"""
                        self.nombre_ingresado = self.nombre_ingresado[0:-1]
            else:
                        self.nombre_ingresado+=evento.unicode
            return self.nombre_ingresado
        
    def devolder_nombre(self):
        """devuelvo lo que el usuario ingreso"""
        return self.nombre_ingresado
    

        