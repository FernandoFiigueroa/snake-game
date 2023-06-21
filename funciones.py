import pygame 
from variables import *
from colores import *
from personaje import Snake
from clase_comida import Comida
from clase_bloque import Bloque
from dibujar_score import imprimir_score
from clase_nombre import Datos
import sys


datos = Datos()
snake = Snake()
food = Comida()
bloque = Bloque()


img_pausa = pygame.image.load("snake_game/imagenes/pausa.png")
img_pausa = pygame.transform.scale(img_pausa,(ALTO_VENTANA,ANCHO_VENTANA )) 
   

def main(ventana,clock,img_galaxia):
        
        """Funcion principal de mi juego, llama a todas las funcion que generan un evento en mi juego"""
        
        correr_juego = True

        tiempo = 0
        segundos = 0
        while correr_juego :
            
            llamar_menu_pausa(ventana)
                          
            clock.tick(FPS) #le da un tiempo al juego para que no valla tan rapido 
            
            ventana.blit(img_galaxia,img_galaxia.get_rect()) #Pego el fondo a la ventana

            while True:
                """Creo un while con la razon de que los bloques no se generen en la misma posicion que la comida del snake"""
                if food.posicion_comida in bloque.bloque_posicion:
                    food.posicion_random()
                break
            
            tiempo += 1
            if tiempo == 15:
                segundos += 1
                tiempo = 0
                
            font_score = pygame.font.SysFont("Helvetica", 20)
            score = font_score.render("TIEMPO: {0}".format(segundos),True,WHITE)
            ventana.blit(score,(0,0)) 
            
            imprimir_funciones(ventana) 
            
        
        
            pygame.display.flip() 



def imprimir_funciones(ventana):
            
            """utilizando OBJETOS llamo a la clase para verificar si la nave se movio. 
            Dibujo la comida del snake,chequeo si mi snake choco con un muro,etc"""
            
            snake.mover_snake(ventana)
            
            chequear_bloque(snake,bloque)
            
            food.dibujar_comida(ventana)  
            
            imprimir_score(ventana,snake,bloque)
            
            chequear_comida(snake,food,ventana)
           


def juego_pausa(ventana):
        
        """Si el usuario llama a la funcion se mostrara una pantalla negra con 2 opciones, la primera es: si sepresiona la tecla Y el juego continua,
        la segunda es:si el ususario presiona la tecla Y el juego se cierra automaticamente """
        
        pausada = True
        while pausada:
            lista_eventos = pygame.event.get()
            for evento in lista_eventos:
                    if evento.type == pygame.QUIT:
                                pygame.quit()
                        
                    if evento.type == pygame.KEYDOWN:
                            if evento.key == pygame.K_x:
                                pausada  = False
                            if evento.key == pygame.K_y:
                                pygame.quit
                                sys.exit()
        
            ventana.blit(img_pausa, (0,0))
            pygame.display.flip()      
        
        
def llamar_menu_pausa(ventana):
    
    """si el usuario oprime la letra q llamo a la funcion juego_pausa()"""
    
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                    pygame.quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_q:
                    juego_pausa(ventana)        
                  
            
def chequear_comida(serpiente,comida,ventana):
    
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
        
