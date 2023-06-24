'''
CLASE JUEGO
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
# pylint: disable=arguments-differ
# pylint: disable=no-member

import sys
import pygame
from modo import *

class Juego():

    def __init__(self, jugador, niveles:list) -> None:

        self.jugador = jugador
        self.nivel_actual = 0
        self.niveles = niveles

    def posicionar_textos(self, pantalla, textos) -> None:

        for texto in textos:
            pantalla.blit(texto['texto'], (texto['pos_x'], texto['pos_y']))

    def manejar_eventos_juego(self, eventos):

        for evento in eventos:

            match evento.type:
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                case pygame.KEYDOWN:
                    if evento.key == pygame.K_TAB:
                        change_mode()

    def update(self, pantalla, fuente, tiempo_transcurrido:float, keys) -> None:

        self.niveles[self.nivel_actual].update(pantalla, self.jugador, keys)

        texto = fuente.render(f"Vidas: {self.jugador.vidas}", False, "Green", "Blue")
        ancho_texto = texto.get_width()

        texto_vidas = {
            "texto": texto,
            "pos_x": pantalla.get_width()-ancho_texto,
            "pos_y": 0
        }

        texto = fuente.render(f"Puntos: {self.jugador.puntos}", False, "Blue")

        texto_puntos = {
            "texto": texto,
            "pos_x": 0,
            "pos_y": 0
        }

        texto = fuente.render(f"Tiempo:{1000-tiempo_transcurrido}", False, "Green", "Blue")
        ancho_texto = texto.get_width()

        texto_tiempo = {
            "texto": texto,
            "pos_x": pantalla.get_width()/2-(ancho_texto/2),
            "pos_y": 0
        }

        textos = [texto_vidas, texto_puntos, texto_tiempo]

        self.posicionar_textos(pantalla, textos)

    def update_personalizado(self) -> None:

        self.niveles[self.nivel_actual].update_personalizado(self.jugador)
