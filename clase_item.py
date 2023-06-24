'''
CLASE ITEM
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
# pylint: disable=arguments-differ
# pylint: disable=no-member

from clase_objeto import Objeto

class Item(Objeto):

    def __init__(self, tamanio: tuple, pos_inicial: tuple, cambio_vida:int,
                 cambio_puntos:int, path_img="", es_trampa=False):
        super().__init__(tamanio, pos_inicial, path_img)

        self.cambio_vida = cambio_vida
        self.cambio_puntos = cambio_puntos
        self.es_trampa = es_trampa
        self.colisiono = False

    # PASAR A JUGADOR
    def verificar_colision_jugador(self, jugador):

        if self.lados['main'].colliderect(jugador.lados['main']):
            self.colisiono = True
            jugador.vidas += self.cambio_vida
            jugador.puntos += self.cambio_puntos

    def update(self, pantalla, jugador):

        self.verificar_colision_jugador(jugador)
        super().update(pantalla)
