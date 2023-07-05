'''
NIVEL 2
'''

import pygame
from clase_item import Item
from clase_nivel import Nivel
from clase_plataforma import Plataforma
from datos_juego import TAMANIO_PANTALLA, W, jugador
from clase_enemigo import Enemigo
from config_img import diccionario_animaciones_yeti_normal, diccionario_animaciones_yeti_rojo

fondo = pygame.image.load("Recursos/Fondos/fondo_nivel_2.png")
fondo = pygame.transform.scale(fondo, TAMANIO_PANTALLA)

enemigo_uno = Enemigo((100,90), (20,0), diccionario_animaciones_yeti_normal,
                      diccionario_animaciones_yeti_rojo,5, -15, 2000, 200,150,3)

enemigo_dos = Enemigo((100,90), (200,0), diccionario_animaciones_yeti_normal,
                      diccionario_animaciones_yeti_rojo,5, -15, 2000, 200, 150,6)

enemigo_uno_inicial = Enemigo((100,90), (20,0), diccionario_animaciones_yeti_normal,
                      diccionario_animaciones_yeti_rojo,5, -15, 2000, 200,150,3)

enemigo_dos_inicial = Enemigo((100,90), (200,0), diccionario_animaciones_yeti_normal,
                      diccionario_animaciones_yeti_rojo,5, -15, 2000, 200, 150,6)

piso_1 = Plataforma((W,20), (0, jugador.lados['bottom'].bottom-1), "Nieve",
                "Recursos/Plataformas/snow_33.png")


plataforma = Plataforma((200,20), (0, 200), "Nieve",
                        "Recursos/Plataformas/snow_33.png")

item_uno = Item((30,50), (0, 450), 10, 0, "Recursos/Obstaculos/coca.png")
item_dos = Item((30,30), (300, 450),0, 100, "Recursos/Obstaculos/hamburguesa.png")

enemigos = [enemigo_uno, enemigo_dos]
enemigos_iniciales = [enemigo_uno_inicial, enemigo_dos_inicial]
lista_plataformas = [piso_1, plataforma]

items = [item_uno, item_dos]

nivel_dos = Nivel(fondo, lista_plataformas,enemigos_iniciales, enemigos,items, 60, 2450,2,7)

# nivel_dos = {"fondo": fondo,
#              "plat": lista_plataformas,
#              "enemigos": enemigos,
#              "items": items,
#              "tiempo": 60,
#              "puntos": 2450,
#              "temp":7
# }