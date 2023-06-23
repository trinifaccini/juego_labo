'''
CLASE OBJETO
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
# pylint: disable=arguments-differ
# pylint: disable=no-member
# pylint: disable=invalid-name

import pygame

from config_img import obtener_rectangulos

class Objeto():

    def __init__(self, tamanio: tuple, pos_inicial:tuple, path_img=""):

        # Si es un objeto inanimado va a tener path_img (ejemplo: plataformas)
        if path_img != "":
            imagen = pygame.image.load(path_img)
            imagen = pygame.transform.scale(imagen, (tamanio[0], tamanio[1]))

        else:
            imagen = pygame.Surface((tamanio[0], tamanio[1]))
            imagen.set_alpha(0) # Transparente

        self.superficie = imagen

        self.w = tamanio[0]
        self.h = tamanio[1]

        rectangulo_img = imagen.get_rect()
        rectangulo_img.x = pos_inicial[0]
        rectangulo_img.y = pos_inicial[1]

        self.lados = obtener_rectangulos(rectangulo_img)

    # Si es un objeto inanimado no va a sobreescribir
    # Si es un objeto animado si va a sobreescribir
    def animar(self,pantalla):
        pantalla.blit(self.superficie, self.lados['main'])

    def update(self, pantalla):
        self.animar(pantalla)
