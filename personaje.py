import pygame 
from colores import *
from variables import *
import random
import tkinter as tk
from tkinter import messagebox as mbox
import sys


class Snake:
    """METODO CONSTRUCTOR"""
    def __init__(self):
        self.velocidad = 20
        self.longitud = 1
        self.cuerpo = [[220,200]] #Si no utilizo una lista dentro de otra lista luego no la puedo iterar
        self.movimiento_actual = random.choice(["right","left","up","down"]) #El personaje comienza de forma random (Si no las declaro en ingles luego no las puedo utilizar)
        self.movimientos_incorrectos = {"right": ["left"],
                                        "left": ["right"],
                                        "up": ["down"],
                                        "down": ["up"]} #Verificio hacia donde no quiero que valla depediendo la direccion
        self.score = 0
        self.best_score = 1
        
    def mover_snake(self,ventana):
            
            """creo eventos y verifico la tecla que el usuario presione, Si oprime la tecla derecha
            el movimiento del personaje va a ser hacia la derecha"""
            
            lista_eventos = pygame.event.get()
            for evento in lista_eventos:
                if evento.type == pygame.QUIT:
                    """Verifico si el usuario cierra la ventana"""
                    pygame.quit() #si no utilizo estte metodo entro un bucle infinito
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        if self.check_valid_movement(pygame.key.name(evento.key)):#necesario que sea en ingles
                            continue
                        self.movimiento_actual = "left"
                        
                    if evento.key == pygame.K_RIGHT:
                        if self.check_valid_movement(pygame.key.name(evento.key)):
                            continue
                        self.movimiento_actual = "right"
                        
                    if evento.key == pygame.K_UP:
                        if self.check_valid_movement(pygame.key.name(evento.key)):
                            continue
                        self.movimiento_actual = "up"
                        
                    if evento.key == pygame.K_DOWN:
                        if self.check_valid_movement(pygame.key.name(evento.key)):
                            continue
                        self.movimiento_actual = "down"
                
            self.snake_movements(ventana)              
            
            
    def snake_movements(self,ventana):
        
        """la funcion hace que la serpiente se mueva constantemente para la direccion en la que el usuario presiono la tecla.
        Por ej: si presion la tecla UP y la solto,la serpiente va a seguir moviendose de igual forma hacia esa direccion"""
        
        if self.movimiento_actual == "left":
            mover = self.cuerpo[0][0] - self.velocidad #Muevo la poscion X
            eje_x = self.check_bounds(mover,"min_limite")
            self.update_snake(eje_x,"X",ventana) #le paso X porque me muevo hacia la izquierda
            
        if self.movimiento_actual == "right":
            mover = self.cuerpo[0][0] + self.velocidad #Muevo la poscion X
            eje_x = self.check_bounds(mover, "max_limite")
            self.update_snake(mover,"X",ventana) #le paso X porque me muevo hacia la izquierda
            
        if self.movimiento_actual == "up":
            mover = self.cuerpo[0][1] - self.velocidad #Muevo la poscion Y
            eje_y = self.check_bounds(mover ,"min_limite")
            self.update_snake(eje_y,"Y",ventana) #le paso X porque me muevo hacia la izquierda
            
        if self.movimiento_actual == "down":
            mover = self.cuerpo[0][1] + self.velocidad #Muevo la poscion Y
            eje_y = self.check_bounds(mover, "max_limite")
            self.update_snake(eje_y,"Y",ventana) #le paso X porque me muevo hacia la izquierda
    
            
    def update_snake(self,valor,llave,ventana):
        """ actualizo lo que verificaba en la funcion snake_movements()"""
        if llave == "X":
            self.cuerpo.insert(0,[valor,self.cuerpo[0][1]]) #inserto los valores en la posicion x
            self.cuerpo.pop()#Eliminito el ultimo elemento de la serpiente(en este caso es el cuerpo)
            self.draw_snake(ventana)
        
        elif llave == "Y":
            self.cuerpo.insert(0,[self.cuerpo[0][0],valor]) #inserto los valores en la posicion x
            self.cuerpo.pop()#Eliminito el ultimo elemento de la serpiente(en este caso es el cuerpo)
            self.draw_snake(ventana)
            
            
    def draw_snake(self,ventana):
        """ imprimo en pantalla los movimientos de la serpiente"""
        for idx, body in enumerate(self.cuerpo): #Con el for recorro los elementos de mi lista( cuerpo de la serpiente)
            """IDX me itera el indice en el cual vamos """
            if idx == 0: 
                """DIBUJO LA CABEZA DE LA SNAKE"""
                pygame.draw.rect(ventana,YELLOW1,(body[0],body[1],20,20))
                continue
            

            pygame.draw.rect(ventana,PURPLE,[body[0],body[1],20,20]) #Dibujo el cuerpo de la snake 
        self.check_error()
    

    def check_valid_movement(self,proxima_tecla):
        """Verifica que si yo presiono la tecla izquierda luego no pueda ir hacia la izquierda,lo mismo en viceversa
        y con la demas teclas"""
        if proxima_tecla in self.movimientos_incorrectos[self.movimiento_actual]:
            return True
         
        
    def check_bounds(self,valor_a_comprobar,limite):
        if limite == "max_limite":
            if valor_a_comprobar > ANCHO_VENTANA: #700 es el valor del alncho de la pantalla
                return 0 # si se pasa que vuelva al inicio            
            else:
                return valor_a_comprobar 
        
        else:
            if valor_a_comprobar < 0: #700 es el valor del alncho de la pantalla
                return 600
            else:
                return valor_a_comprobar   

    def obtener_cabeza(self):
        """unicamente retorna la posicion de la cabeza de la serpiente"""    
        return self.cuerpo[0]    
    
    
    def crecer_serpiente(self,valor,ventana):
        
        """Funcion para hacer la serpiente aumente su tamaño. 
        Inserto el valor que recibo por parametro en la pos 0 de mi snake"""
        
        self.cuerpo.insert(0,list(valor))
        self.draw_snake(ventana)


    def check_error(self):
        """Cheque si la snake si choca consigo misma,si es asi la reseata"""
        if self.obtener_cabeza() in self.cuerpo[2:]:
            self.reset() #llamo a la funcion reset para volver a 1 a la snake
            self.score = 0
    
    
    def reset(self):
        """Reseteo el cuerpo de mi snake"""
        self.mensaje_derrota(self.longitud)
        self.cuerpo = [[220,220]] #modifico todo el cuerpo menos la cabeza
        self.movimiento_actual = random.choice(["right","left","up","down"]) #al cambiar el cuerpo tengo que volver a elegir dirrecion

        if self.longitud > self.score:
            self.score = self.longitud
        self.score = 0 #si cho mi score queda en 0
        self.longitud = 1  
        

    def mensaje_derrota(self,score):
        """Funcion que me muestra un mensaje con mi score al perder"""
        raiz = tk.Tk()
        raiz.withdraw()
        mbox.showerror("PERDISTE!","Tu score es : {0}".format(score))
        try:
            raiz.destroy()#destruye un widget
        
        except:
            pass
        sys.exit()
        
