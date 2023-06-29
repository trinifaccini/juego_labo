'''
MAIN
'''

# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=no-member
# pylint: disable=invalid-name

import sys
import pygame
from clase_juego import Juego
from config_db import *
from config_img import dibujar_borde_rectangulos
from datos_juego import W,H,TAMANIO_PANTALLA, FPS, jugador
from datos_nivel_tres import nivel_tres
from datos_nivel_dos import nivel_dos
from datos_nivel_uno import nivel_uno
from API_FORMS.GUI_form_inicio import FormInicio
from modo import get_mode

pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMANIO_PANTALLA)

FUENTE = pygame.font.Font("Recursos/Fonts/Snowes.ttf", 60)


# Timer para el juego
TIMER_EVENT = pygame.USEREVENT + 0
pygame.time.set_timer(TIMER_EVENT, 1000)

juego = None
form_inicio = FormInicio(PANTALLA, 50, 25, W-100, H-50,"Recursos/Fondos/bg-icebergs-2.png")


niveles = [nivel_uno, nivel_dos, nivel_tres]

while True:

    RELOJ.tick(FPS)
    eventos = pygame.event.get()

    keys = pygame.key.get_pressed()

    if form_inicio.flag_jugar:

        if juego is None:
            juego = Juego(jugador, form_inicio.nivel, "jugadores.db", form_inicio.usuario_jugador, niveles)

        juego.manejar_eventos_juego(PANTALLA, eventos)

        for evento in eventos:
            if evento.type == TIMER_EVENT:
                juego.niveles[juego.nivel_actual].tiempo -= 1
                juego.update_personalizado(PANTALLA, keys)

        juego.update(PANTALLA, FUENTE, keys)

        if get_mode() is True:

            for p in juego.niveles[juego.nivel_actual].plataformas:
                dibujar_borde_rectangulos(PANTALLA, p.lados, "Green")

            for e in juego.niveles[juego.nivel_actual].enemigos:
                dibujar_borde_rectangulos(PANTALLA, e.lados, "Blue")
                for x in e.lista_proyectiles:
                    dibujar_borde_rectangulos(PANTALLA, x.lados, "Magenta")

            dibujar_borde_rectangulos(PANTALLA, juego.jugador.lados, "Red")

            for i in juego.niveles[juego.nivel_actual].items:
                dibujar_borde_rectangulos(PANTALLA, i.lados, "Yellow")

        pygame.display.flip()

    else:

        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        PANTALLA.fill("Black")
        form_inicio.update(eventos)

    pygame.display.flip()
