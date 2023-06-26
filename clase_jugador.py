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

    # VERIFICO COLISION DE ITEM CON PERSONAE JUGADOR UNICAMENTE
    # SI COLISIONA LO BORRO DE LA LISTA
    def verificar_colision_items(self, items):

        for item in items:
            if self.lados['main'].colliderect(item.lados['main']):
                item.colisiono = True
                self.vidas += item.cambio_vida
                self.puntos += item.cambio_puntos
                print("COLISIONO ITEM")
                lista_aux = items
                lista_aux.remove(item)
                del item

    def verificar_colision_enemigos(self, enemigos):

        for enemigo in enemigos:
            if enemigo.accion == "ataca":
                self.vidas -= enemigo.danio

    def definir_accion(self, keys):

        if keys[pygame.K_RIGHT]:
            self.accion = "derecha"
        elif keys[pygame.K_LEFT]:
            self.accion = "izquierda"
        elif keys[pygame.K_UP]:
            self.accion = "salta"
        else:
            self.accion = "quieto"

    def update(self, pantalla, lista_plataformas, enemigos, items, keys):

        self.verificar_colision_items(items)
        self.definir_accion(keys)

        super().update(pantalla, lista_plataformas, enemigos)


    def update_personalizado(self, enemigos, keys):

        # Verifico la colision unicamente aca porque este update se llama
        # cada un segundo
        self.verificar_colision_enemigos(enemigos)

        if keys[pygame.K_SPACE]:
            self.lanzar_proyectil(10)
