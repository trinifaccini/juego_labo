'''
CLASE ITEM
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
# pylint: disable=arguments-differ
# pylint: disable=no-member

import copy
from clase_objeto import Objeto

def deepcopy_item(item):

    tamanio = copy.deepcopy(item.tamanio)
    pos_inicial = copy.deepcopy(item.pos_inicial)
    cambio_vida = copy.deepcopy(item.cambio_vida)
    cambio_puntos = copy.deepcopy(item.cambio_puntos)
    path_img = copy.deepcopy(item.path_img)
    es_trampa = copy.deepcopy(item.es_trampa)

    item = Item(tamanio, pos_inicial, cambio_vida, cambio_puntos,path_img, es_trampa)

    return item


class Item(Objeto):

    def __init__(self, tamanio: tuple, pos_inicial: tuple, cambio_vida:int,
                 cambio_puntos:int, path_img="", es_trampa=False):
        super().__init__(tamanio, pos_inicial, path_img)

        self.cambio_vida = cambio_vida
        self.cambio_puntos = cambio_puntos
        self.es_trampa = es_trampa
        self.colisiono = False
