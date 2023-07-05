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
from config_img import deepcopy_dict_animaciones
import copy

from datos_juego import W

def deepcopy_enemigo(enemigo, vidas):

    tamanio = copy.deepcopy(enemigo.tamanio)
    pos_inicial = copy.deepcopy(enemigo.pos_inicial)

    animaciones_aux_normal = deepcopy_dict_animaciones(enemigo.animaciones[0])
    animaciones_aux_danio = deepcopy_dict_animaciones(enemigo.animaciones[1])

    velocidad = 20
    potencia_salto = copy.deepcopy(enemigo.potencia_salto)
    danio =  copy.deepcopy(enemigo.danio)
    aporte_puntos =  copy.deepcopy(enemigo.aporte_puntos)
    temporizador =  copy.deepcopy(enemigo.temporizador)

    enemigo = Enemigo(tamanio, pos_inicial, animaciones_aux_normal, animaciones_aux_danio, velocidad,
                   potencia_salto, vidas,danio,aporte_puntos,temporizador)
    
    enemigo.superficie_apoyo = None

    return enemigo



class Enemigo(Personaje):

    def __init__(self, tamanio: tuple, pos_inicial: tuple, animaciones_normal, animaciones_danio,
                 velocidad: int, potencia_salto: int, vidas: int, danio: int, aporte_puntos:int, temporizador:int):
        
        super().__init__(tamanio, pos_inicial, animaciones_normal, animaciones_danio,
                         velocidad, potencia_salto, vidas, danio)


        self.accion = "derecha"
        self.ultima_accion = "derecha"
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

        print(self.lados['left'].x)
        print(self.lados['main'].x)

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
                        print("cambia de lado a izq")
                        self.accion = "izquierda"

                elif (self.accion == "izquierda" and self.lados['left'].x <= 2):
                        self.accion = "derecha"
                        print("cambia de lado a der")

    def update(self, pantalla, lista_plataformas, personajes):

        self.definir_accion(personajes[0])
        self.atacar(pantalla)

        super().update(pantalla, lista_plataformas, personajes)
