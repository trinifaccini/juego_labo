import pygame
from clase_objeto_animado import ObjetoAnimado
from clase_proyectil import Proyectil


class Personaje(ObjetoAnimado):
    
    def __init__(self, tamanio: tuple, pos_inicial: tuple, animaciones, velocidad: int, potencia_salto: int, vidas:int, img_proyectil:str, danio:int):
        super().__init__(tamanio, pos_inicial, animaciones, velocidad, potencia_salto)

        self.vidas = vidas
        self.img_proyectil = img_proyectil
        self.lista_proyectiles = []
        self.danio = danio


    def lanzar_proyectil(self):

        # print(self.lados['main'].centerx)
        # print(self.lados['main'].centery)

        vel = 10

        if self.accion == "izquierda":
            vel = vel * -1

        proyectil = Proyectil(
            (20, 20),(self.lados['main'].centerx, self.lados['left'].y), -20, 0, vel, self.img_proyectil)

        self.lista_proyectiles.append(proyectil)

    def definir_accion(self):
        
        self.accion = "quieto"

    
