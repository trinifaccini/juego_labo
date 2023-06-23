'''
CLASE JUGADOR
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
# pylint: disable=arguments-differ
# pylint: disable=no-member

import pygame
from clase_personaje import Personaje

class Jugador(Personaje):

    def __init__(self, tamanio: tuple, pos_inicial: tuple, animaciones, velocidad: int,
                 potencia_salto: int, vidas: int, img_proyectil: str, danio: int):

        super().__init__(tamanio, pos_inicial, animaciones, velocidad, potencia_salto,
                         vidas, img_proyectil, danio)

        self.accion = "derecha"
        self.puntos = 0

    def definir_accion(self, keys):

        if keys[pygame.K_RIGHT]:
            self.accion = "derecha"
        elif keys[pygame.K_LEFT]:
            self.accion = "izquierda"
        elif keys[pygame.K_UP]:
            self.accion = "salta"
        elif keys[pygame.K_SPACE]:
            self.accion = "ataca"
        else:
            self.accion = "quieto"

    def update(self, pantalla, lista_plataformas, keys):

        self.definir_accion(keys)
        super().update(pantalla, lista_plataformas)
