import pygame, sys
from clase_enemigo import Enemigo
from clase_item import Item
from clase_juego import Juego
from clase_jugador import Jugador
from clase_nivel import Nivel
from clase_objeto import Objeto
from clase_objeto_animado import ObjetoAnimado
from config_img import * 
from funciones_juego import *

pygame.init()

W = 1200
H = 600
FPS = 18

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W, H))

fuente = pygame.font.Font("Recursos/Fonts/Snowes.ttf", 60)

path = "Recursos/Obstaculos/bola_nieve_1.png"

# JUEGO
jugador = Jugador((50,50), (200,H-70), diccionario_animaciones_personaje, 5, -15, 3000, "Recursos/Obstaculos/bola_nieve_1.png", 100)

# NIVEL UNO

fondo_uno = pygame.image.load("Recursos/Fondos/fondo_negro.png")
fondo_uno = pygame.transform.scale(fondo_uno, (W,H))

enemigo_uno = Enemigo((50,50), (20,0), diccionario_animaciones_yeti, 5, -15, 2000, "Recursos/Obstaculos/bola_nieve_1.png", 200)
enemigo_dos = Enemigo((50,50), (500,0), diccionario_animaciones_yeti, 5, -15, 2000, "Recursos/Obstaculos/bola_nieve_1.png", 200)

piso = Objeto((W,20), (0, jugador.lados['bottom'].bottom-1), "Recursos/Plataformas/plataforma_tierra_nieve.png")
plataforma = Objeto((200,20), (0, 200), "Recursos/Plataformas/plataforma_tierra_nieve.png")

item_uno = Item((30,50), (0, 450), 10, 0, "Recursos/Obstaculos/coca.png")
item_dos = Item((30,30), (200, 450),0, 10, "Recursos/Obstaculos/hamburguesa.png")

enemigos = [enemigo_uno, enemigo_dos]
lista_plataformas = [piso, plataforma]
items = [item_uno, item_dos]

nivel_uno = Nivel(fondo_uno, lista_plataformas,enemigos, items)
juego = Juego(jugador, [nivel_uno])


# def definir_accion_personaje(keys, jugador):

#     if keys[pygame.K_RIGHT]:
#         jugador.accion = "derecha"
#     elif keys[pygame.K_LEFT]:
#         jugador.accion = "izquierda"
#     elif keys[pygame.K_UP] or keys[pygame.K_SPACE]:
#         jugador.accion = "salta"
#     else:
#         jugador.accion = "quieto"

tiempo = 0

# Timer para el juego
TIMER_EVENT = pygame.USEREVENT + 0
pygame.time.set_timer(TIMER_EVENT, 1000)

elementos_juego = [jugador, enemigos, lista_plataformas, items]


while True:

    RELOJ.tick(FPS)

    eventos = pygame.event.get()

    juego.manejar_eventos_juego(eventos)

    for evento in eventos:
        if evento.type == TIMER_EVENT:
            tiempo += 1
            if tiempo % 5 == 0:
                for e in enemigos:
                    e.lanzar_proyectil()

    PANTALLA.fill("Black")

    if jugador.vidas == 0:
        juego.nivel_actual = 1

    juego.update(PANTALLA, fuente, tiempo, pygame.key.get_pressed())

    # jugador.update(PANTALLA, lista_plataformas, pygame.key.get_pressed())
    # dibujar_borde_rectangulos(PANTALLA, jugador.lados, "Pink")

    # for p in lista_plataformas:
    #     p.update(PANTALLA)
    #     dibujar_borde_rectangulos(PANTALLA, p.lados, "Red")

    # for e in enemigos:
    #     funciones_enemigo(e, PANTALLA, lista_plataformas, jugador)

    # funciones_items(items, PANTALLA, jugador)

    pygame.display.flip()
