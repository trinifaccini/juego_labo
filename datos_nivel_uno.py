'''
NIVEL UNO
'''

import pygame
import copy
from clase_item import Item
from clase_nivel import Nivel
from clase_plataforma import Plataforma
from datos_juego import TAMANIO_PANTALLA, W, H
from clase_enemigo import Enemigo, deepcopy_enemigo
from config_img import diccionario_animaciones_oso_normal, diccionario_animaciones_oso_rojo

fondo = pygame.image.load("Recursos/Fondos/aldea__.png")
fondo = pygame.transform.scale(fondo, TAMANIO_PANTALLA)

enemigo_uno = Enemigo((70,60), (200,0), diccionario_animaciones_oso_normal,
                      diccionario_animaciones_oso_rojo, 3, -15, 100, 200,100,5)

# enemigo_dos = Enemigo((70,60), (600,0), diccionario_animaciones_oso_normal,
#                       diccionario_animaciones_oso_rojo, 3, -15, 100, 200,100,10)

enemigo_dos = deepcopy_enemigo(enemigo_uno, 200)

enemigo_uno_inicial = Enemigo((100,90), (200,0), diccionario_animaciones_oso_normal,
                      diccionario_animaciones_oso_rojo, 3, -15, 100, 200,100,5)

enemigo_dos_inicial  = Enemigo((100,90), (600,0), diccionario_animaciones_oso_normal,
                      diccionario_animaciones_oso_rojo, 3, -15, 100, 200,100,10)


piso = Plataforma((W,20), (0, H-20), "Nieve",
                "Recursos/Plataformas/plataforma_grande.png")


plataforma_1 = Plataforma((200,20), (0, 500), "Tierra",
                        "Recursos/Plataformas/plataforma_tierra_nieve.png")


plataforma_2 = Plataforma((200,20), (300, 435), "Tierra",
                        "Recursos/Plataformas/plataforma_tierra_nieve.png")

plataforma_3 = Plataforma((200,20), (600, 400), "Tierra",
                        "Recursos/Plataformas/plataforma_tierra_nieve.png")

plataforma_4 = Plataforma((200,20), (W-200-100, 300), "Tierra",
                        "Recursos/Plataformas/plataforma_tierra_nieve.png")


item_uno = Item((30,50), (0, 450), 10, 0, "Recursos/Obstaculos/coca.png")
item_dos = Item((30,30), (200, 450),0, 10, "Recursos/Obstaculos/hamburguesa.png")

trampa_uno = Item((30,100), (plataforma_1.lados['main'].x+50, plataforma_1.lados['top'].y-100),
                  -10, 0, "Recursos/Obstaculos/snow_108.png", True)

trampa_dos = Item((50,50), (plataforma_3.lados['main'].x, plataforma_3.lados['top'].y-50),
                  0, -10, "Recursos/Obstaculos/snow_1b.png", True)

enemigos = [enemigo_uno, enemigo_dos]
enemigos_iniciales = [enemigo_uno_inicial, enemigo_dos_inicial]
lista_plataformas = [piso, plataforma_1, plataforma_2, plataforma_3, plataforma_4]

items = [item_uno, item_dos]
trampas = [trampa_uno, trampa_dos]

nivel_uno = Nivel(fondo, lista_plataformas, enemigos_iniciales, enemigos, items,trampas, 30, 220,1,30)


# nivel_uno = {"fondo": fondo,
#              "plat": lista_plataformas,
#              "enemigos": enemigos,
#              "items": items,
#              "tiempo": 30,
#              "puntos": 220,
#              "temp":10
# }
