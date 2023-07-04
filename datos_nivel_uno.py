'''
NIVEL UNO
'''

import pygame
from clase_item import Item
from clase_nivel import Nivel
from clase_plataforma import Plataforma
from datos_juego import TAMANIO_PANTALLA, W, jugador
from clase_enemigo import Enemigo
from config_img import diccionario_animaciones_oso_normal, diccionario_animaciones_oso_rojo

fondo = pygame.image.load("Recursos/Fondos/aldea__.png")
fondo = pygame.transform.scale(fondo, TAMANIO_PANTALLA)

enemigo_uno = Enemigo((100,90), (200,0), diccionario_animaciones_oso_normal,
                      diccionario_animaciones_oso_rojo, 5, -15, 100, 200,100,5)

enemigo_dos = Enemigo((100,90), (600,0), diccionario_animaciones_oso_normal,
                      diccionario_animaciones_oso_rojo, 5, -15, 100, 200,100,10)


piso = Plataforma((W,20), (0, jugador.lados['bottom'].bottom-1), "Nieve",
                "Recursos/Plataformas/plataforma_grande.png")


plataforma_1 = Plataforma((200,20), (0, 500), "Tierra",
                        "Recursos/Plataformas/plataforma_tierra_nieve.png")


plataforma_2 = Plataforma((200,20), (300, 500), "Tierra",
                        "Recursos/Plataformas/plataforma_tierra_nieve.png")

plataforma_3 = Plataforma((200,20), (500, 400), "Tierra",
                        "Recursos/Plataformas/plataforma_tierra_nieve.png")

plataforma_4 = Plataforma((200,20), (W-200, 300), "Tierra",
                        "Recursos/Plataformas/plataforma_tierra_nieve.png")


item_uno = Item((30,50), (0, 450), 10, 0, "Recursos/Obstaculos/coca.png")
item_dos = Item((30,30), (200, 450),0, 10, "Recursos/Obstaculos/hamburguesa.png")

enemigos = [enemigo_uno, enemigo_dos]
lista_plataformas = [piso, plataforma_1, plataforma_2, plataforma_3, plataforma_4]

items = [item_uno, item_dos]

nivel_uno = Nivel(fondo, lista_plataformas, enemigos, items, 30, 220,1,10)
