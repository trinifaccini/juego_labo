'''
MAIN
'''

# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=no-member
# pylint: disable=invalid-name

import pygame
from clase_juego import Juego
from config_db import *
from config_img import dibujar_borde_rectangulos
from datos_juego import TAMANIO_PANTALLA, FPS, jugador
from datos_nivel_tres import nivel_tres
from datos_nivel_dos import nivel_dos
from datos_nivel_uno import nivel_uno
from modo import get_mode

pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMANIO_PANTALLA)

FUENTE = pygame.font.Font("Recursos/Fonts/Snowes.ttf", 60)


# Timer para el juego
TIMER_EVENT = pygame.USEREVENT + 0
pygame.time.set_timer(TIMER_EVENT, 1000)

nuevo_usuario = input("Sos un usuario nuevo? S o N: ")

if nuevo_usuario == "N":

    usuario = input("Ingresa tu usuario: ")

    existe = buscar_usuario_db("jugadores.db", usuario)

    while len(existe) == 0:
        usuario = input("Usuario inexistente. Ingresa tu nombre de usuario")
        existe = buscar_usuario_db("jugadores.db", usuario)

    guardado = True

else:

    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    usuario = input("Ingresa tu usuario: ")

    guardado = insertar_jugador(nombre, apellido, 0, 0, usuario, "jugadores.db")

    while guardado is False:
        usuario = input("Usuario existente. Ingresa otro usuario: ")
        guardado = insertar_jugador(nombre, apellido, 0, 0, usuario, "jugadores.db")

if guardado:
    juego = Juego(jugador, "jugadores.db", usuario, [nivel_uno, nivel_dos, nivel_tres])


while True and juego:

    RELOJ.tick(FPS)

    eventos = pygame.event.get()

    juego.manejar_eventos_juego(eventos)

    keys = pygame.key.get_pressed()

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
