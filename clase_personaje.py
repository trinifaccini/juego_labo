'''
CLASE PERSONAJE
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=arguments-differ

import pygame
from clase_objeto_animado import ObjetoAnimado
from clase_proyectil import Proyectil
from config_img import deepcopy_dict_animaciones

class Personaje(ObjetoAnimado):

    def __init__(self, tamanio: tuple, pos_inicial: tuple, animaciones_normal, animaciones_danio,
                 velocidad: int, potencia_salto: int, vidas:int, danio:int):

        animaciones_aux_normal = deepcopy_dict_animaciones(animaciones_normal)
        animaciones_aux_danio = deepcopy_dict_animaciones(animaciones_danio)

        lista = [animaciones_aux_normal, animaciones_aux_danio]

        super().__init__(tamanio, pos_inicial, lista, velocidad, potencia_salto)

        pygame.mixer.init()

        self.vidas = vidas
        self.img_proyectil = "Recursos/Obstaculos/bola_nieve_1.png"
        self.lista_proyectiles = []
        self.danio = danio

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
                self.lados["main"].bottom = plat.lados['main'].top
                self.desplazamiento_y = 0
                break
            else:
                self.esta_saltando = True

    def lanzar_proyectil(self, velocidad):

        if self.ultima_accion == "izquierda":
            velocidad = velocidad * -1

        proyectil = Proyectil(
            (20, 20),(self.lados['main'].centerx, self.lados['left'].centery),-self.danio,
            0, velocidad, self.img_proyectil)

        self.lista_proyectiles.append(proyectil)

    def update_proyectiles(self, pantalla):

        lista_aux = self.lista_proyectiles
        for proyectil in self.lista_proyectiles:
            proyectil.update(pantalla)
            # ACA REMOVER DE PANTALLA
            if proyectil.verificar_colision_pantalla(pantalla):
                lista_aux.remove(proyectil)


    # En el caso del jugador, va a ser manipulado por el usuario
    # En el caso del enemigo, va a ser manipulado por los choques
    def definir_accion(self):

        self.accion = "quieto"

    def definir_animacion(self, pantalla) -> None:

        if self.superficie_apoyo is not None:
            if self.accion == "derecha":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_derecha")
                if self.lados['main'].x < pantalla.get_width() - self.w + 10:
                    self.ultima_accion = "derecha"
                    self.mover("x")
            elif self.accion == "izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_izquierda")
                if self.lados['main'].x > 0:
                    self.ultima_accion = "izquierda"
                    self.mover("x")
            elif self.accion == "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
            elif self.accion == "quieto":
                if not self.esta_saltando: # solo animo si no está saltando
                    if self.ultima_accion == "derecha":
                        self.animar(pantalla, "quieto_derecha")
                    else:
                        self.animar(pantalla, "quieto_izquierda")


    def update(self, pantalla, lista_plataformas):

        self.definir_animacion(pantalla)
        self.update_proyectiles(pantalla)
        self.verificar_salto(pantalla)
        self.verificar_colision_pisos(lista_plataformas)
