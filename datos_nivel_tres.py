'''
NIVEL 3
'''

import pygame
from clase_boss import Boss
from clase_item import Item
from clase_nivel import Nivel
from clase_plataforma import Plataforma
from datos_juego import TAMANIO_PANTALLA, W,jugador
from clase_enemigo import Enemigo
from config_img import diccionario_animaciones_yeti_normal, diccionario_animaciones_yeti_rojo

fondo = pygame.image.load("Recursos/Fondos/fondo_nivel_3.png")
fondo = pygame.transform.scale(fondo, TAMANIO_PANTALLA)

enemigo_uno_inicial = Boss((300,200), (200,0), diccionario_animaciones_yeti_normal,
                      diccionario_animaciones_yeti_rojo,5, -15, 2000, 200, 300,7)

enemigo_uno = Boss((200,150), (200,0), diccionario_animaciones_yeti_normal,
                      diccionario_animaciones_yeti_rojo,7, -15, 2000, 200, 300,5)


piso_1 = Plataforma((W,20), (0, jugador.lados['bottom'].bottom-1), "Tierra",
                "Recursos/Plataformas/plataforma_grande.png")


plataforma = Plataforma((200,20), (0, 200),"Tierra",
                        "Recursos/Plataformas/plataforma_tierra_nieve.png")

item_uno = Item((30,50), (0, 450), 10, 0, "Recursos/Obstaculos/coca.png")
item_dos = Item((30,30), (300, 450),0, 10, "Recursos/Obstaculos/hamburguesa.png")

enemigos_iniciales = [enemigo_uno_inicial]
enemigos = [enemigo_uno]
lista_plataformas = [piso_1, plataforma]

items = [item_uno, item_dos]
trampas = []


nivel_tres = Nivel(fondo, lista_plataformas,enemigos_iniciales,enemigos, items,trampas, 60, 7600,3,5)

# nivel_tres = {"fondo": fondo,
#              "plat": lista_plataformas,
#              "enemigos": enemigos,
#              "items": items,
#              "tiempo": 60,
#              "puntos": 8000,
#              "temp":5
# }