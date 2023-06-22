# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

import pygame
from clase_objeto_animado import ObjetoAnimado
from clase_personaje import Personaje
from clase_proyectil import Proyectil


class Enemigo(Personaje):

    def __init__(self, tamanio: tuple, pos_inicial: tuple, animaciones, velocidad: int, potencia_salto: int, vidas: int, img_proyectil: str, danio: int):
        
        super().__init__(tamanio, pos_inicial, animaciones, velocidad, potencia_salto, vidas, img_proyectil, danio)

        self.accion = "derecha"
        self.esta_saltando = True

    def definir_accion(self):

        # REBOTE SOBRE LA PLATAFORMA EN LA QUE SE ENCUENTRA

        if self.superficie_apoyo is not None:
            if (self.accion == "derecha" and
                self.lados['right'].x == self.superficie_apoyo.lados['main'].x + self.superficie_apoyo.lados['main'].width):
                
                self.accion = "izquierda"

            elif self.accion == "izquierda" and self.lados['left'].x == self.superficie_apoyo.lados['main'].x:
                self.accion = "derecha"

    def update(self, pantalla, lista_plataformas):

        self.definir_accion()
        super().update(pantalla, lista_plataformas)




       

    