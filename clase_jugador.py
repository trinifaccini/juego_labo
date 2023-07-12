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
from clase_proyectil import Proyectil

class Jugador(Personaje):

    def __init__(self, tamanio: tuple, pos_inicial: tuple, animaciones_normal, animaciones_danio,
                 velocidad: int,potencia_salto: int, vidas: int, danio: int):

        super().__init__(tamanio, pos_inicial, animaciones_normal, animaciones_danio,
                         velocidad, potencia_salto, vidas, danio)

        pygame.mixer.init()

        self.vidas_iniciales = vidas
        self.puntos = 0
        #self.sonido_colision_item = pygame.mixer.Sound('Recursos/Audio/coin.mp3')
        self.sonido_colision_proyectil = pygame.mixer.Sound('Recursos/Audio/snowball.mp3')
        self.sonido_colision_trampa  = pygame.mixer.Sound('Recursos/Audio/ouch.mp3')
        self.volumen = 5
        self.cooldown_count = 0

    def cooldown(self) -> None:

        if self.cooldown_count >= 10:
            self.cooldown_count = 0
        elif self.cooldown_count > 0:
            self.cooldown_count += 1

    # VERIFICO COLISION DE ITEM CON PERSONAJE JUGADOR UNICAMENTE
    # SI COLISIONA LO BORRO DE LA LISTA
    def verificar_colision_items_especiales(self, items):

        for item in items:
            if self.lados['main'].colliderect(item.lados['main']):
                if item.es_trampa is False:
                    sound = pygame.mixer.Sound(item.path_sonido)
                    sound.set_volume(self.volumen)
                    sound.play()
                    self.vidas += item.cambio_vida
                    self.puntos += item.cambio_puntos
                    lista_aux = items
                    lista_aux.remove(item)
                    del item

    def verificar_colision_trampas(self, trampas):

        for item in trampas:
            if (self.lados['right'].colliderect(item.lados['main']) or
                                               self.lados['left'].colliderect(item.lados['main'])):
                self.accion = "atacado"


    def daniar_por_trampas(self, trampas):

        for item in trampas:
            if (self.lados['right'].colliderect(item.lados['main']) or
                                               self.lados['left'].colliderect(item.lados['main'])):
                self.vidas += item.cambio_vida
                self.puntos += item.cambio_puntos
                self.sonido_colision_trampa.set_volume(self.volumen)
                self.sonido_colision_trampa.play()


    # SI VEO LO DE QUE SEA CADA UN SEGUNDO USAR ESTE METODO
    def verificar_colision_enemigos(self, enemigos):

        for enemigo in enemigos:
            if enemigo.accion == "ataca":
                self.sonido_colision_trampa.set_volume(self.volumen)
                self.sonido_colision_trampa.play()
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
                break

            self.esta_saltando = True
            self.velocidad = 5

    def daniar_personaje_por_enemigo(self, enemigos):

        for enemigo in enemigos:
            if enemigo.accion == "ataca":
                self.vidas -= enemigo.danio


    def lanzar_proyectil(self, velocidad, keys):

        self.cooldown()

        if keys[pygame.K_SPACE] and self.accion != "inmovilizado" and self.cooldown_count == 0:

            if self.ultima_accion == "izquierda":
                velocidad = velocidad * -1

            proyectil = Proyectil(
                (20, 20),(self.lados['main'].centerx, self.lados['left'].centery),-self.danio, 0,
                velocidad, "Recursos/Obstaculos/bola_nieve_1.png")
            
            self.lista_proyectiles.append(proyectil)
            self.cooldown_count = 1


    def verificar_proyectil_golpeo_jugador(self, enemigos) -> None:

        for enemigo in enemigos:
            for proyectil in enemigo.lista_proyectiles:
                if proyectil.lados['main'].colliderect(self.lados['main']):
                    self.sonido_colision_proyectil.set_volume(self.volumen)
                    self.sonido_colision_proyectil.play()
                    self.animaciones_actual = self.animaciones[1]
                    self.vidas += proyectil.cambio_vida
                    lista_aux = enemigo.lista_proyectiles
                    lista_aux.remove(proyectil)
                    del proyectil
                    return True
                else:
                    self.animaciones_actual = self.animaciones[0]
                    return False

    def verificar_proyectil_golpeo_enemigo(self, lista_enemigos) -> None:

        for enemigo in lista_enemigos:
            for proyectil in self.lista_proyectiles:
                if enemigo.superficie_apoyo is not None:
                    if proyectil.lados['main'].colliderect(enemigo.lados['main']):
                        enemigo.animaciones_actual = enemigo.animaciones[1]
                        enemigo.vidas += proyectil.cambio_vida
                        lista_aux = self.lista_proyectiles
                        lista_aux.remove(proyectil)
                        del proyectil
                    else:
                        enemigo.animaciones_actual = enemigo.animaciones[0]

    def verificar_animacion_atacado(self, pantalla) -> None:

        if self.accion == "atacado":
            if self.ultima_accion == "derecha":
                self.animar(pantalla, "atacado_derecha")
            else:
                self.animar(pantalla, "atacado_izquierda")

        if self.accion == "inmovilizado":
            if self.ultima_accion == "derecha":
                self.animar(pantalla, "escondido_derecha")
            else:
                self.animar(pantalla, "escondido_izquierda")

    def definir_animacion(self, pantalla) -> None:

        self.verificar_animacion_atacado(pantalla)
        super().definir_animacion(pantalla)

    def definir_accion(self, keys):

        if self.accion != "inmovilizado":
            if keys[pygame.K_RIGHT]:
                self.accion = "derecha"
            elif keys[pygame.K_LEFT]:
                self.accion = "izquierda"
            elif keys[pygame.K_UP]:
                self.accion = "salta"
            elif self.accion != "atacado":
                self.accion = "quieto"


    def update(self, pantalla, lista_plataformas, enemigos, items,trampas, keys):

        self.definir_accion(keys)
        self.lanzar_proyectil(10, keys)
        super().update(pantalla, lista_plataformas)

        self.verificar_colision_items_especiales(items)
        self.verificar_colision_trampas(trampas)
        self.verificar_proyectil_golpeo_enemigo(enemigos)
        self.verificar_proyectil_golpeo_jugador(enemigos)


    def update_personalizado(self, enemigos,trampas):

        self.verificar_colision_enemigos(enemigos)
        self.daniar_personaje_por_enemigo(enemigos)
        self.daniar_por_trampas(trampas)
