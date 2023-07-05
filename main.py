'''
MAIN
'''

# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=no-member
# pylint: disable=invalid-name

import sys
import pygame
from API_FORMS.GUI_pantalla_final import FormFinal
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
form_final = None

niveles = [nivel_uno, nivel_dos, nivel_tres]

while True:

    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    keys = pygame.key.get_pressed()

    if juego is not None:
        form_inicio.flag_jugar = juego.jugando

    if form_inicio.flag_jugar is False:

        juego = None
        form_final = None

        PANTALLA.fill("Black")
        form_inicio.update(eventos)

    elif juego is not None and juego.estado_juego is not None:

        PANTALLA.fill("Black")

        if form_final is None:
            form_final = FormFinal(PANTALLA, 50, 25, W-100, H-50,
                                   "Recursos/Fondos/bg-icebergs-2.png",juego.estado_juego)
        form_final.update(eventos, juego)

        if form_final.estado_juego is None:
            juego = None
            form_inicio.flag_jugar = False

    else:

        if juego is None:

            juego = Juego(PANTALLA, jugador, form_inicio.nivel, "jugadores.db",
                          form_inicio.usuario_jugador, niveles)

            if form_inicio.nivel == 0:
                jugador.puntos = 0
            else:
                jugador.puntos = juego.niveles[juego.nivel_actual-1].puntos_requeridos

            juego.reiniciar_tiempo_vidas_juego()

        juego.manejar_eventos_juego(PANTALLA, eventos)

        for evento in eventos:
            if evento.type == TIMER_EVENT:
                juego.niveles[juego.nivel_actual].tiempo -= 1
                juego.update_personalizado(PANTALLA, keys)

        juego.update(PANTALLA, FUENTE, eventos, keys)

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

    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    pygame.display.flip()
