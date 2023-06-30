'''
CLASE JUGADOR
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
# pylint: disable=arguments-differ
# pylint: disable=no-member
# pylint: disable=too-many-arguments

import pygame
from clase_personaje import Personaje

class Jugador(Personaje):

    def __init__(self, tamanio: tuple, pos_inicial: tuple, animaciones_normal, animaciones_danio, velocidad: int,
                 potencia_salto: int, vidas: int, danio: int):

        super().__init__(tamanio, pos_inicial, animaciones_normal, animaciones_danio,
                         velocidad, potencia_salto,vidas, danio)

        self.accion = "derecha"
        self.puntos = 0

    # VERIFICO COLISION DE ITEM CON PERSONAJE JUGADOR UNICAMENTE
    # SI COLISIONA LO BORRO DE LA LISTA
    def verificar_colision_items(self, items):

        for item in items:
            if self.lados['main'].colliderect(item.lados['main']):
                self.vidas += item.cambio_vida
                self.puntos += item.cambio_puntos
                item.colisiono = True
                # lista_aux = items
                # lista_aux.remove(item)
                # del item


    # SI VEO LO DE QUE SEA CADA UN SEGUNDO USAR ESTE METODO
    def verificar_colision_enemigos(self, enemigos):

        for enemigo in enemigos:
            if enemigo.accion == "ataca":
                self.vidas -= enemigo.danio
                self.accion = "atacado"

    def verificar_colision_pisos(self, lista_plataformas):

            for plat in lista_plataformas:
                if self.lados['bottom'].colliderect(plat.lados['top']):
                    if self.superficie_apoyo is None:
                        self.superficie_apoyo = plat
                    self.esta_saltando = False
                    self.lados["main"].bottom = plat.lados['main'].top + 5
                    self.desplazamiento_y = 0
                    self.velocidad = plat.alteracion_velocidad
                    print(plat.alteracion_velocidad)
                    break
                else:
                    self.esta_saltando = True
                    self.velocidad = 5

    def daniar_personaje_por_enemigo(self, enemigos):

        for enemigo in enemigos:
            if enemigo.accion == "ataca":
                self.vidas -= enemigo.danio

    def definir_accion(self, keys):

        if keys[pygame.K_RIGHT]:
            self.accion = "derecha"
        elif keys[pygame.K_LEFT]:
            self.accion = "izquierda"
        elif keys[pygame.K_UP]:
            self.accion = "salta"
        elif self.accion != "atacado":
            self.accion = "quieto"

    def update(self, pantalla, lista_plataformas, enemigos, items, keys):

        self.verificar_colision_items(items)
        self.definir_accion(keys)

        if self.accion == "atacado":
            if self.ultima_accion == "derecha":
                self.animar(pantalla, "atacado_derecha")
            else:
                self.animar(pantalla, "atacado_izquierda")

        super().update(pantalla, lista_plataformas, enemigos)


    def update_personalizado(self, enemigos, pantalla, keys):

        # Verifico la colision unicamente aca porque este update se llama
        # cada un segundo

        #self.verificar_colision_enemigos(enemigos, pantalla)

        self.daniar_personaje_por_enemigo(enemigos)

        if keys[pygame.K_SPACE]:
            self.lanzar_proyectil(10)
