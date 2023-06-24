'''
CLASE PROYECTIL
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
# pylint: disable=arguments-differ
# pylint: disable=no-member

from clase_item import Item

class Proyectil(Item):

    def __init__(self, tamanio: tuple, pos_inicial: tuple, cambio_vida: int, cambio_puntos: int,
                 velocidad, path_img="", es_trampa=False):

        super().__init__(tamanio, pos_inicial, cambio_vida, cambio_puntos, path_img, es_trampa)

        self.velocidad = velocidad


    def verificar_colision_pantalla(self, pantalla):

        if self.velocidad > 0 and self.lados['right'].x >= pantalla.get_width()-self.w*2:
            self.colisiono = True

        elif self.velocidad < 0 and self.lados['left'].x <= 30:
            self.colisiono = True

    def mover(self) -> None:

        # La direccion del proyectil va a estar dada por la velocidad
        for lado in dict(self.lados):
            self.lados[lado].x += self.velocidad

    def update(self, pantalla) -> None:

        self.verificar_colision_pantalla(pantalla)
        self.mover()
        super().update(pantalla)