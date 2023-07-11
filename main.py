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
from API_FORMS.GUI_pantalla_final import FormFinal
from API_FORMS.GUI_form_inicio import FormInicio
from modo import get_mode

pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMANIO_PANTALLA)

FUENTE = pygame.font.Font("Recursos/Fonts/Snowes.ttf", 45)

# Timer para el juego
TIMER_EVENT = pygame.USEREVENT + 0
pygame.time.set_timer(TIMER_EVENT, 1000)

juego = None
form_inicio = FormInicio(PANTALLA, 50, 25, W-100, H-50,"Recursos/Fondos/bg-icebergs-2.png")
form_final = None

def dibujar_borde_rectangulos_juego(pantalla, juego_param) -> None:

    '''
    Dibuja los rectangulos de las superficies de todo el juego
    '''

    if get_mode() is True:

        for p in juego_param.niveles[juego_param.nivel_actual].plataformas:
            dibujar_borde_rectangulos(pantalla, p.lados, "Green")

        for e in juego_param.niveles[juego_param.nivel_actual].enemigos:
            dibujar_borde_rectangulos(pantalla, e.lados, "Blue")
            for x in e.lista_proyectiles:
                dibujar_borde_rectangulos(pantalla, x.lados, "Magenta")

        dibujar_borde_rectangulos(pantalla, juego_param.jugador.lados, "Red")

        for i in juego_param.niveles[juego_param.nivel_actual].items:
            dibujar_borde_rectangulos(pantalla, i.lados, "Yellow")

def tiempo_en_segundos (eventos_juego,juego_param) -> None:

    '''
    Cuenta el tiempo en segundos del juego
    '''

    for e in eventos_juego:
        if e.type == TIMER_EVENT:
            juego_param.niveles[juego_param.nivel_actual].tiempo -= 1
            juego_param.update_personalizado()

while True:

    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    keys = pygame.key.get_pressed()

    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    if juego is not None and juego.jugando is False:
        form_inicio.flag_jugar = juego.jugando

    if form_inicio.flag_jugar is False:

        form_final = None
        PANTALLA.fill("Black")
        form_inicio.update(eventos)
        juego = None


    elif juego is not None and juego.estado_juego is not None:

        PANTALLA.fill("Black")

        if form_final is None:
            form_final = FormFinal(PANTALLA, 50, 25, W-100, H-50,
                                   "Recursos/Fondos/bg-icebergs-2.png",juego.estado_juego, 
                                   juego.jugador.puntos)

        form_final.update(eventos)

        if form_final.estado_juego == "again":
            juego = None
            form_inicio.flag_jugar = False
            form_inicio = FormInicio(PANTALLA, 50, 25, W-100, H-50,
                                     "Recursos/Fondos/bg-icebergs-2.png")
    else:

        if juego is None:

            juego = Juego(PANTALLA, jugador, form_inicio.nivel, "jugadores.db",
                          form_inicio.usuario_jugador)

            if form_inicio.nivel == 0:
                jugador.puntos = 0

            juego.reiniciar_juego()

            juego.mostrar_form_nivel()

        juego.manejar_eventos_juego(eventos)
        tiempo_en_segundos(eventos  , juego)
        juego.update(PANTALLA, FUENTE, eventos, keys)
        dibujar_borde_rectangulos_juego(PANTALLA, juego)

    pygame.display.flip()
