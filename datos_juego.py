from clase_jugador import Jugador
from config_img import diccionario_animaciones_personaje_normal, diccionario_animaciones_personaje_rojo


W = 1200
H = 600
FPS = 22

TAMANIO_PANTALLA = (W,H)

jugador = Jugador((60,80), (200,H-100), diccionario_animaciones_personaje_normal,
                  diccionario_animaciones_personaje_rojo,5, -15,
                  1100, 300)
