import pygame 
from variables import *
from colores import *
from personaje import Snake
from clase_comida import Comida
from clase_bloque import Bloque
from dibujar_score import imprimir_score
from clase_nombre import Datos
from crear_base_de_datos import insertar_datos_en_BD
import sys


datos = Datos()
snake = Snake()
food = Comida()
bloque = Bloque()

   
def main(ventana,clock,img_galaxia,nombre_ingresado):
        
        """Funcion principal de mi juego, llama a todas las funcion que generan un evento en mi juego"""
        correr_juego = True

        tiempo = 0
        segundos = 0
        while correr_juego :
            clock.tick(FPS) #le da un tiempo al juego para que no valla tan rapido 
            
           

            ventana.blit(img_galaxia,img_galaxia.get_rect()) #Pego el fondo a la ventana

            while True:
                """Creo un while con la razon de que los bloques no se generen en la misma posicion que la comida del snake"""
                if food.posicion_comida in bloque.bloque_posicion:
                    food.posicion_random()
                break
            
            
            tiempo += 1
            if tiempo == 20:
                segundos += 1
                tiempo = 0
                
                
            font_score = pygame.font.SysFont("Helvetica", 20)
            score = font_score.render("TIEMPO: {0}".format(segundos),True,WHITE)
            ventana.blit(score,(0,0)) 

            imprimir_funciones(ventana,nombre_ingresado) #imprimo toda mi funciones de eventos
            pygame.display.flip() 




def imprimir_funciones(ventana,nombre_ingresado):
            
            """utilizando OBJETOS llamo a la clase para verificar si la nave se movio. 
            Dibujo la comida del snake,chequeo si mi snake choco con un muro,etc"""
            
            snake.mover_snake(ventana)
            chequear_bloque(snake,bloque)
            chequear_comida(snake,food,ventana,nombre_ingresado)
            food.dibujar_comida(ventana)  
            imprimir_score(ventana,snake,bloque)
            
            
            
def chequear_comida(serpiente,comida,ventana,nombre_ingresado):
    
    """La funcion verifica si la posicion de la cabeza de mi snake es la misma que la de la manzana. En pocas palabras verifica si la snake se comio la manzana.
        Si la condicion se cumple se vuelve a generar una posicion random de la manzana, tambien aumentamos el score"""
    
    if tuple(serpiente.obtener_cabeza()) == comida.posicion_comida: #como el metodo obtener_cabeza() me devuelve una lista lo casteo a una tupla para que se puedan comparars(#si le pongo un (in) lo pasa por arriba)
        
        serpiente.crecer_serpiente(comida.posicion_comida,ventana)
        
        comida.posicion_random()
        comida.dibujar_comida(ventana)
        
        serpiente.longitud+=1
        if serpiente.longitud > serpiente.best_score:
            serpiente.best_score += 1
            """ le paso a mi base de datos mi score"""
            insertar_datos_en_BD(serpiente.score,nombre_ingresado)
  
  
        
def chequear_bloque(serpiente,bloque):
    
        """La funcion verifica si la posicion de mi snake es la misma que la de los bloques, si esto se cumple se vuelven a gener muros en otras posiciones 
            y mi snake vuelve a empeza solamente con la cabeza"""
            
        if tuple(serpiente.obtener_cabeza()) in bloque.bloque_posicion: #si le pongo un ==  lo pasa por arriba
            bloque.posicion_random()
            serpiente.reset()




def draw_ingreso_nombre(ventana,img_fondo,nombre_ingresado):
        """creo un rectangulo en el cual dentro el usuario puede escribir su nombre antes de comenzar el juego"""
        
        font_input = pygame.font.SysFont("arial",30)
        
        ingreso_rect = pygame.Rect(X_RECT_INGRESO,Y_RECT_INGRESO,ANCHO_RECT_INGRESO,ALTO_RECT_INGRESO) #CREO EL RECTANGULO CON TAMÑO Y POSICION
        
        ventana.blit(img_fondo,img_fondo.get_rect()) #imprimo la imagen de fondo para que no sea un fondo negro
        
        pygame.draw.rect(ventana,BLACK,ingreso_rect,TAMAÑO_RECT_INGRESO) #imprimo el cuadrado en el cual el usuario ingresa los datos
        
        font_rect = font_input.render(nombre_ingresado,True,WHITE)#Le doy una fuente a las letras que el usuario ingrese como dato
        
        ventana.blit(font_rect,(ingreso_rect.x +5,ingreso_rect.y +5)) #imprimo lo que el usuario escribe dentro del cuadrado
        
      

