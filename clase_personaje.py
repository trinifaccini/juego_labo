'''
CLASE PERSONAJE
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from clase_objeto_animado import ObjetoAnimado
from clase_proyectil import Proyectil

class Personaje(ObjetoAnimado):

    def __init__(self, tamanio: tuple, pos_inicial: tuple, animaciones, velocidad: int,
                 potencia_salto: int, vidas:int, img_proyectil:str, danio:int):

        super().__init__(tamanio, pos_inicial, animaciones, velocidad, potencia_salto)

        self.vidas = vidas
        self.img_proyectil = img_proyectil
        self.lista_proyectiles = []
        self.danio = danio


    def lanzar_proyectil(self, velocidad):

        if self.accion == "izquierda":
            velocidad = velocidad * -1

        proyectil = Proyectil(
            (20, 20),(self.lados['main'].centerx, self.lados['left'].y),
            -500, 0, velocidad, self.img_proyectil)

        self.lista_proyectiles.append(proyectil)

    def definir_accion(self):

        self.accion = "quieto"
