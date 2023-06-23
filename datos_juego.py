from clase_jugador import Jugador
from config_img import diccionario_animaciones_personaje


W = 1200
H = 600
FPS = 18

TAMANIO_PANTALLA = (W,H)

jugador = Jugador((60,80), (200,H-100), diccionario_animaciones_personaje, 5, -15, 3000, "Recursos/Obstaculos/bola_nieve_1.png", 100)
