'''
CLASE ENEMIGO
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
# pylint: disable=arguments-differ
# pylint: disable=no-member

from clase_enemigo import Enemigo
from clase_proyectil import Proyectil
import copy

from config_img import deepcopy_dict_animaciones

def deepcopy_boss(enemigo):

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

    enemigo = Boss(tamanio, pos_inicial, animaciones_aux_normal, animaciones_aux_danio, velocidad,
                   potencia_salto, vidas,danio,aporte_puntos,temporizador)

    enemigo.superficie_apoyo = None

    return enemigo

class Boss(Enemigo):

    def __init__(self, tamanio: tuple, pos_inicial: tuple, animaciones_normal, animaciones_danio,
                 velocidad: int, potencia_salto: int, vidas: int, danio: int, aporte_puntos:int, temporizador:int):
        
        super().__init__(tamanio, pos_inicial, animaciones_normal, animaciones_danio,
                         velocidad, potencia_salto, vidas, danio, aporte_puntos,temporizador)

    def lanzar_proyectil(self, velocidad):

        velocidad = velocidad * 1.5

        if self.ultima_accion == "izquierda":
            velocidad = velocidad * -1

        proyectil = Proyectil(
            (50, 50),(self.lados['main'].centerx, self.lados['left'].centery),
            -500, 0, velocidad, "Recursos/Obstaculos/piedra.png")

        self.lista_proyectiles.append(proyectil)

    def verificar_colision_items_especiales(self, items):

        for item in items:
            if self.lados['main'].colliderect(item.lados['main']):
                if item.es_trampa is not True:
                    item.colisiono = True

    def atacar_especial(self, pantalla):

        if self.accion == "ataque_especial":
            if self.ultima_accion == "izquierda":
                self.animar(pantalla, "ataca_especial_izquierda")
            elif self.ultima_accion == "derecha":
                self.animar(pantalla, "ataca_especial_derecha")

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
                if tiempo % 5 == 0:
                    self.accion = "ataque_especial"
                    jugador.accion = "inmovilizado"
                else:
                    self.accion = self.ultima_accion
                    jugador.accion = jugador.ultima_accion
                    
                if self.accion == "ataca":
                    self.accion = self.ultima_accion

                if (self.accion == "derecha" and self.lados['right'].x >= self.superficie_apoyo.lados['right'].x):
                        self.accion = "izquierda"

                elif (self.accion == "izquierda" and (self.lados['left'].x <= 2 or self.lados['left'].x <=  self.superficie_apoyo.lados['left'].x+2)):
                        self.accion = "derecha"
    
    def update(self, pantalla, lista_plataformas, items, personajes, tiempo):

        self.verificar_colision_items_especiales(items)
        self.atacar_especial(pantalla)
        super().update(pantalla, lista_plataformas, personajes, tiempo)

    