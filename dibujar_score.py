import pygame
from colores import * 
from variables import *
    



def imprimir_score(ventana,snake,bloque):
        font_score = pygame.font.SysFont("Helvetica", 20) #creo la fuente del score
        font_pausa = pygame.font.SysFont("Oswald", 20) 
        
        """Creo un texto y lo pego en la pantalla"""    
        score = font_score.render("score: {0}".format(snake.longitud),True,WHITE)
        ventana.blit(score,(ANCHO_VENTANA-130,0))   
        score = font_score.render("best score: {0}".format(snake.best_score),True,WHITE)
        ventana.blit(score,(ANCHO_VENTANA-130,20))  
        score = font_pausa.render("Presiona Q para pausar el juego",True,WHITE)
        ventana.blit(score,(ANCHO_VENTANA-400,20))  
        bloque.dibujar_bloque(ventana)