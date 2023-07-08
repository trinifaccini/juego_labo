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

enemigo_uno = Enemigo((70,80), (20,0), diccionario_animaciones_yeti_normal,
                      diccionario_animaciones_yeti_rojo,5, -15, 450, 200,150,3)

enemigo_dos = Enemigo((70,80), (700,0), diccionario_animaciones_yeti_normal,
                      diccionario_animaciones_yeti_rojo,5, -15, 450, 200, 150,6)

piso = Plataforma((W,20), (0, jugador.lados['bottom'].bottom-1), "Nieve",
                "Recursos/Plataformas/snow_33.png")


plataforma_1 = Plataforma((250,20), (100, 200), "Nieve",
                        "Recursos/Plataformas/snow_33.png")

plataforma_2 = Plataforma((250,20), (450, 300), "Nieve",
                        "Recursos/Plataformas/snow_33.png")

plataforma_3 = Plataforma((200,20), (700, 400), "Nieve",
                        "Recursos/Plataformas/snow_33.png")

plataforma_4 = Plataforma((100,20), (950, 460), "Nieve",
                        "Recursos/Plataformas/snow_33.png")

plataforma_5 = Plataforma((50,20), (375, 270), "Nieve",
                        "Recursos/Plataformas/snow_33.png")


trampa_uno = Item((40,120), (plataforma_1.lados['main'].x+50, plataforma_1.lados['top'].y-120),
                  -10, 0, "Recursos/Obstaculos/winter-tree-2.png", True)

trampa_dos = Item((50,50), (plataforma_2.lados['main'].x+15, plataforma_2.lados['top'].y-50),
                  0, -10, "Recursos/Obstaculos/snow_2b.png", True)

trampa_tres = Item((50,50), (plataforma_3.lados['main'].x+55, plataforma_3.lados['top'].y-50),
                  0, -10, "Recursos/Obstaculos/snow_2a.png", True)

trampa_cuatro = Item((30,150), (piso.lados['main'].x+60, piso.lados['top'].y-150),
                  0, -10, "Recursos/Obstaculos/winter-tree-3.png", True)


item_uno = Item((30,50), (plataforma_1.lados['main'].x, plataforma_1.lados['main'].y-50),
                10, 0, "Recursos/Obstaculos/coca.png")

item_dos = Item((30,30), (300, 450),0, 100, "Recursos/Obstaculos/hamburguesa.png")

enemigos = [enemigo_uno, enemigo_dos]
lista_plataformas = [piso, plataforma_1, plataforma_2, plataforma_3, plataforma_4, plataforma_5]

items = [item_uno, item_dos]
trampas = [trampa_uno, trampa_dos, trampa_tres, trampa_cuatro]

nivel_dos = Nivel(fondo, lista_plataformas, enemigos,items,trampas, 60, 6,3,2,12)

# nivel_dos = {"fondo": fondo,
#              "plat": lista_plataformas,
#              "enemigos": enemigos,
#              "items": items,
#              "tiempo": 60,
#              "puntos": 2450,
#              "temp":7
# }