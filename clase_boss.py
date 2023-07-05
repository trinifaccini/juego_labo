'''
CLASE ENEMIGO
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
# pylint: disable=arguments-differ
# pylint: disable=no-member

from clase_enemigo import Enemigo
from clase_proyectil import Proyectil


class Boss(Enemigo):

    def __init__(self, tamanio: tuple, pos_inicial: tuple, animaciones_normal, animaciones_danio,
                 velocidad: int, potencia_salto: int, vidas: int, danio: int, aporte_puntos:int, temporizador:int):
        
        super().__init__(tamanio, pos_inicial, animaciones_normal, animaciones_danio,
                         velocidad, potencia_salto, vidas, danio, aporte_puntos,temporizador)

    def lanzar_proyectil(self, velocidad):

        velocidad = velocidad * 1.5

        if self.ultima_accion == "izquierda":
            velocidad = velocidad * -1

        proyectil = Proyectil(
            (50, 50),(self.lados['main'].centerx, self.lados['left'].centery),
            -500, 0, velocidad)

        self.lista_proyectiles.append(proyectil)
        
    def verificar_colision_items_especiales(self, items):

        for item in items:
            if self.lados['main'].colliderect(item.lados['main']):
                if item.es_trampa is not True:
                    item.colisiono = True
    

    def update(self, pantalla, lista_plataformas, items, personajes):

        self.verificar_colision_items_especiales(items)
        super().update(pantalla, lista_plataformas, personajes)
