
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

    def __init__(self, tamanio: tuple, pos_inicial: tuple, animaciones,
                 velocidad:int, potencia_salto: int):

        super().__init__(tamanio, pos_inicial, "")

        self.contador_pasos = 0

        animaciones_aux = deepcopy_dict_animaciones(animaciones)

        self.animaciones = animaciones_aux

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

        imagenes_accion = self.animaciones[accion]

        # cuantas imagenes tengo para esa accion en particular
        largo = len(imagenes_accion)

        # necesito saber si el contador de pasos es mayor a la
        # cantidad de imagenes que tengo para la animacion
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(imagenes_accion[self.contador_pasos], self.lados['main'])
        self.contador_pasos += 1

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagen(self.animaciones[clave], self.w, self.h)

    def mover(self, eje:str):

        for lado in dict(self.lados):

            if eje == "x":
                if self.accion == "izquierda":
                    self.lados[lado].x += self.velocidad*-1
                else:
                    self.lados[lado].x += self.velocidad
            else:
                self.lados[lado].y += self.desplazamiento_y

    def verificar_salto(self, pantalla):

        if self.esta_saltando:
            if self.ultima_accion == "derecha":
                self.animar(pantalla, "salta_derecha")
            else:
                self.animar(pantalla, "salta_izquierda")

            self.mover("y")

            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

    def verificar_colision_pisos(self, lista_plataformas):

        for plat in lista_plataformas:
            if self.lados['bottom'].colliderect(plat.lados['top']):
                if self.superficie_apoyo is None:
                    self.superficie_apoyo = plat
                self.esta_saltando = False
                self.lados["main"].bottom = plat.lados['main'].top + 5
                self.desplazamiento_y = 0
                break
            else:
                self.esta_saltando = True

    def atacar(self, pantalla):

        if self.ultima_accion == "izquierda":
            if "ataca_izquierda" in self.animaciones:
                self.animar(pantalla, "ataca_izquierda")
            else:
                self.animar(pantalla, "camina_izquierda")

        elif self.ultima_accion == "derecha":
            if "ataca_derecha" in self.animaciones:
                self.animar(pantalla, "ataca_derecha")
            else:
                self.animar(pantalla, "camina_izquierda")


    def update(self, pantalla, lista_plataformas):

        # En el caso del jugador, va a ser manipulado por el usuario
        # En el caso del enemigo, va a ser manipulado por los choques

        if self.superficie_apoyo is not None:
            match (self.accion):
                case "derecha":
                    if not self.esta_saltando:
                        self.animar(pantalla, "camina_derecha")
                    if self.lados['main'].x < pantalla.get_width() - self.w + 10:
                        self.ultima_accion = "derecha"
                        self.mover("x")
                case "izquierda":
                    if not self.esta_saltando:
                        self.animar(pantalla, "camina_izquierda")
                    if self.lados['main'].x > 0:
                        self.ultima_accion = "izquierda"
                        self.mover("x")
                case "salta":
                    if not self.esta_saltando:
                        self.esta_saltando = True
                        self.desplazamiento_y = self.potencia_salto
                case "ataca":
                    if not self.esta_saltando:
                        self.atacar(pantalla)
                        print("atacando")
                case "quieto":
                    if not self.esta_saltando: # solo animo si no está saltando
                        if self.ultima_accion == "derecha":
                            self.animar(pantalla, "quieto_derecha")
                        else:
                            self.animar(pantalla, "quieto_izquierda")

        self.verificar_salto(pantalla)
        self.verificar_colision_pisos(lista_plataformas)
