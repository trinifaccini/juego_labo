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
from clase_proyectil import Proyectil
from config_img import deepcopy_dict_animaciones
import copy


def deepcopy_enemigo(enemigo):

    tamanio = copy.deepcopy(enemigo.tamanio)
    pos_inicial = copy.deepcopy(enemigo.pos_inicial)

    animaciones_aux_normal = deepcopy_dict_animaciones(enemigo.animaciones[0])
    animaciones_aux_danio = deepcopy_dict_animaciones(enemigo.animaciones[1])

    velocidad = copy.deepcopy(enemigo.velocidad)
    potencia_salto = copy.deepcopy(enemigo.potencia_salto)
    danio =  copy.deepcopy(enemigo.danio)
    aporte_puntos =  copy.deepcopy(enemigo.aporte_puntos)
    temporizador =  copy.deepcopy(enemigo.temporizador)
    vidas = copy.deepcopy(enemigo.vidas)

    enemigo = Enemigo(tamanio, pos_inicial, animaciones_aux_normal, animaciones_aux_danio, velocidad,
                   potencia_salto, vidas,danio,aporte_puntos,temporizador)

    enemigo.superficie_apoyo = None

    return enemigo

class Enemigo(Personaje):

    def __init__(self, tamanio: tuple, pos_inicial: tuple, animaciones_normal, animaciones_danio,
                 velocidad: int, potencia_salto: int, vidas: int, danio: int, aporte_puntos:int,
                 temporizador:int):

        super().__init__(tamanio, pos_inicial, animaciones_normal, animaciones_danio,
                         velocidad, potencia_salto, vidas, danio)

        self.ultima_accion = "derecha"
        self.esta_saltando = True
        self.aporte_puntos = aporte_puntos
        self.temporizador = temporizador

    def verificar_animacion_ataque(self, pantalla):

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

    def definir_animacion(self, pantalla) -> None:

        self.verificar_animacion_ataque(pantalla)
        super().definir_animacion(pantalla)

    def definir_accion(self, jugador, tiempo):

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

                if (self.accion == "derecha" and self.lados['right'].x >= self.superficie_apoyo.lados['right'].x):
                        self.accion = "izquierda"

                elif (self.accion == "izquierda" and (self.lados['left'].x <= 2 or self.lados['left'].x <=  self.superficie_apoyo.lados['left'].x+2)):
                        self.accion = "derecha"

    def update(self, pantalla, lista_plataformas, personajes,tiempo):

        self.definir_accion(personajes[0],tiempo)
        super().update(pantalla, lista_plataformas)

    def update_personalizado(self, tiempo) -> None:

        if self.superficie_apoyo is not None:
            if tiempo % self.temporizador == 0 and self.accion != "ataca":
              self.lanzar_proyectil(15)
