
'''
CLASE OBJETO ANIMADO
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
# pylint: disable=arguments-differ
# pylint: disable=no-member

from clase_objeto import Objeto
from config_img import *


class ObjetoAnimado(Objeto):

    def __init__(self, tamanio: tuple, pos_inicial: tuple, animaciones:list,
                 velocidad:int, potencia_salto: int):

        super().__init__(tamanio, pos_inicial, "")

        self.contador_pasos = 0

        self.animaciones = animaciones
        self.animaciones_actual = animaciones[0]

        self.accion = "derecha"
        self.ultima_accion = "derecha"

        self.velocidad = velocidad
        self.esta_saltando = False

        self.superficie_apoyo = None

        self.desplazamiento_y = 0
        self.gravedad = 1 # cuanto mas grande, mas rapido cae
        self.potencia_salto = potencia_salto
        self.limite_velocidad_caida = potencia_salto*-1

        self.reescalar_animaciones()

    def animar(self, pantalla, accion: str):

        imagenes_accion = self.animaciones_actual[accion]

        # cuantas imagenes tengo para esa accion en particular
        largo = len(imagenes_accion)

        # necesito saber si el contador de pasos es mayor a la
        # cantidad de imagenes que tengo para la animacion
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(imagenes_accion[self.contador_pasos], self.lados['main'])
        self.contador_pasos += 1

    def reescalar_animaciones(self):
        for dict_animaciones in self.animaciones:
            for clave in dict_animaciones:
                reescalar_imagen(dict_animaciones[clave], self.w, self.h)

    def mover(self, eje:str):

        for lado in dict(self.lados):

            if eje == "x":
                if self.accion == "izquierda":
                    self.lados[lado].x += self.velocidad*-1
                else:
                    self.lados[lado].x += self.velocidad
            else:
                self.lados[lado].y += self.desplazamiento_y



    def update(self):
        pass
