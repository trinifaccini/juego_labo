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

    def __init__(self, tamanio: tuple, pos_inicial: tuple, animaciones, velocidad: int,
                 potencia_salto: int, vidas: int, img_proyectil: str, danio: int):

        super().__init__(tamanio, pos_inicial, animaciones, velocidad, potencia_salto,
                         vidas, img_proyectil, danio)

        self.accion = "derecha"
        self.esta_saltando = True


    def definir_accion(self, jugador):

        # REBOTE SOBRE LA PLATAFORMA EN LA QUE SE ENCUENTRA

        if self.superficie_apoyo is not None:

            if (self.ultima_accion == "derecha" and
                jugador.lados['main'].colliderect(self.lados['right'])):
                    self.accion = "ataca"
            
            elif (self.ultima_accion == "izquierda" and
                  jugador.lados['main'].colliderect(self.lados['left'])):
                    self.accion = "ataca"

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
        super().update(pantalla, lista_plataformas, personajes)
