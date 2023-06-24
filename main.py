# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=no-member
# pylint: disable=invalid-name

import pygame
from clase_juego import Juego
from config_img import dibujar_borde_rectangulos
from datos_juego import TAMANIO_PANTALLA, FPS, jugador
from datos_nivel_dos import nivel_dos
from datos_nivel_uno import nivel_uno, nivel_tres
from modo import get_mode

pygame.init()


RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMANIO_PANTALLA)

FUENTE = pygame.font.Font("Recursos/Fonts/Snowes.ttf", 60)

juego = Juego(jugador, [nivel_uno, nivel_dos, nivel_tres])

tiempo = 0

# Timer para el juego
TIMER_EVENT = pygame.USEREVENT + 0
pygame.time.set_timer(TIMER_EVENT, 1000)


while True:

    RELOJ.tick(FPS)

    eventos = pygame.event.get()

    juego.manejar_eventos_juego(eventos)

    keys = pygame.key.get_pressed()

    for evento in eventos:
        if evento.type == TIMER_EVENT:
            juego.niveles[juego.nivel_actual].tiempo -= 1
            if juego.niveles[juego.nivel_actual].tiempo % 5 == 0:
                for e in juego.niveles[juego.nivel_actual].enemigos:
                    e.lanzar_proyectil(15)
            if jugador.puntos >= juego.niveles[juego.nivel_actual].puntos_requeridos:
                juego.nivel_actual += 1
            juego.update_personalizado(keys)

    if juego.niveles[juego.nivel_actual].tiempo <= 0 and jugador.puntos < juego.niveles[juego.nivel_actual].puntos_requeridos:
        print("NO ALCANZO LOS PUNTOS")
        juego.cerrar_juego()

    if jugador.vidas <= 0:
        print("MUERTO")
        juego.cerrar_juego()

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
