'''
NIVEL 2
'''

import pygame
from clase_item import Item
from clase_nivel import Nivel
from clase_objeto import Objeto
from datos_juego import TAMANIO_PANTALLA, W, jugador
from clase_enemigo import Enemigo
from config_img import diccionario_animaciones_yeti_normal, diccionario_animaciones_yeti_rojo

fondo = pygame.image.load("Recursos/Fondos/aldea.png")
fondo = pygame.transform.scale(fondo, TAMANIO_PANTALLA)

enemigo_uno = Enemigo((100,90), (20,0), diccionario_animaciones_yeti_normal,
                      diccionario_animaciones_yeti_rojo,5, -15, 2000, 200)

enemigo_dos = Enemigo((100,90), (200,0), diccionario_animaciones_yeti_normal,
                      diccionario_animaciones_yeti_rojo,5, -15, 2000, 200)

piso_1 = Objeto((W,20), (0, jugador.lados['bottom'].bottom-1),
                "Recursos/Plataformas/plataforma_grande.png")

piso_2 = Objeto((W,20), (0, jugador.lados['bottom'].bottom-1),
                "Recursos/Plataformas/plataforma_grande.png")

plataforma = Objeto((200,20), (0, 200), "Recursos/Plataformas/plataforma_tierra_nieve.png")

item_uno = Item((30,50), (0, 450), 10, 0, "Recursos/Obstaculos/coca.png")
item_dos = Item((30,30), (300, 450),0, 100, "Recursos/Obstaculos/hamburguesa.png")

enemigos = [enemigo_uno, enemigo_dos]
lista_plataformas = [piso_1, piso_2, plataforma]

items = [item_uno, item_dos]

nivel_dos = Nivel(fondo, lista_plataformas,enemigos, items, 60, 2450)
