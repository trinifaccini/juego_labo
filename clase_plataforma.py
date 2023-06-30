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

class Plataforma(Objeto):

    def __init__(self, tamanio: tuple, pos_inicial: tuple, tipo, path_img):
        super().__init__(tamanio, pos_inicial, path_img)

        if tipo == "Tierra":
            self.alteracion_velocidad = 5
        elif tipo == "Nieve":
            self.alteracion_velocidad = 7
        elif tipo == "Hielo":
            self.alteracion_velocidad = 10
