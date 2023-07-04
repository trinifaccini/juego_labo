'''
CLASE ENEMIGO
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
# pylint: disable=arguments-differ
# pylint: disable=no-member

from clase_personaje import Personaje


class Enemigo(Personaje):

    def __init__(self, tamanio: tuple, pos_inicial: tuple, animaciones_normal, animaciones_danio,
                 velocidad: int, potencia_salto: int, vidas: int, danio: int, aporte_puntos:int, temporizador:int):

        super().__init__(tamanio, pos_inicial, animaciones_normal, animaciones_danio,
                         velocidad, potencia_salto, vidas, danio)

        self.accion = "derecha"
        self.esta_saltando = True
        self.aporte_puntos = aporte_puntos
        self.temporizador = temporizador

    def atacar(self, pantalla):

        if self.accion == "ataca":
            if self.ultima_accion == "izquierda":
                if "ataca_izquierda" in self.animaciones_actual:
                    self.animar(pantalla, "ataca_izquierda")
                else:
                    self.animar(pantalla, "camina_izquierda")

            elif self.ultima_accion == "derecha":
                if "ataca_derecha" in self.animaciones_actual:
                    self.animar(pantalla, "ataca_derecha")
                else:
                    self.animar(pantalla, "camina_derecha")


    def definir_accion(self, jugador):

        # REBOTE SOBRE LA PLATAFORMA EN LA QUE SE ENCUENTRA

        if self.superficie_apoyo is not None:
            if (self.ultima_accion == "derecha" and
                jugador.lados['main'].colliderect(self.lados['right'])):
                self.accion = "ataca"
                jugador.accion = "atacado" # SI VEO LO DE QUE SEA CADA UN SEGUNDO SACAR

            elif (self.ultima_accion == "izquierda" and
                  jugador.lados['main'].colliderect(self.lados['left'])):
                self.accion = "ataca"
                jugador.accion = "atacado" # SI VEO LO DE QUE SEA CADA UN SEGUNDO SACAR

            else:
                if self.accion == "ataca":
                    self.accion = self.ultima_accion

                if (self.accion == "derecha" and
                    self.lados['right'].x == (self.superficie_apoyo.lados['main'].x +
                                            self.superficie_apoyo.lados['main'].width)):

                    self.accion = "izquierda"

                elif (self.accion == "izquierda" and
                    self.lados['left'].x == self.superficie_apoyo.lados['main'].x):
                    self.accion = "derecha"

    def update(self, pantalla, lista_plataformas, personajes):

        self.definir_accion(personajes[0])
        self.atacar(pantalla)

        super().update(pantalla, lista_plataformas, personajes)
