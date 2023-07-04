# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=too-many-arguments

'''
ARCHIVO CLASE NIVEL
'''

import random
from clase_enemigo import Enemigo
from clase_item import Item
from config_img import *

class Nivel():

    def __init__(self, fondo, plataformas:list, enemigos:list,
                 items:list, tiempo:int, puntos_requeridos:int, nivel:int, temporizador) -> None:

        self.fondo = fondo
        self.tiempo = tiempo
        self.enemigos = enemigos
        self.items = items
        self.plataformas = plataformas # las plataformas van a venir con las trampas
        self.nivel = nivel
        self.puntos_requeridos = puntos_requeridos
        self.temporizador = temporizador

    def generar_proyectiles(self) -> None:

        for enemigo in self.enemigos:
            if self.tiempo % enemigo.temporizador == 0:
                enemigo.lanzar_proyectil(15)

    def enemigo_segun_nivel(self) -> Enemigo:

        danio = random.randint(100, 200)
        temporizador = random.randint(3, 10)
        danio = random.randint(5, 10)

        if self.nivel == 1:
            return Enemigo((100,90), (200,0), diccionario_animaciones_oso_normal,
                                diccionario_animaciones_oso_rojo, 5, -15, 2000,
                                danio,200,temporizador)

        if self.nivel == 2:
            return Enemigo((100,90), (200,0), diccionario_animaciones_yeti_normal,
                            diccionario_animaciones_oso_rojo, 5, -15, 2000,
                            danio,200,temporizador)

    def generar_enemigos(self) -> None:

        if self.tiempo % self.temporizador == 0:
            enemigo = self.enemigo_segun_nivel()
            self.enemigos.append(enemigo)

    def generar_items_especiales(self) -> None:

        if self.tiempo % 10 == 0:
            item_uno = Item((30,50), (0, 450), 10, 0, "Recursos/Obstaculos/coca.png")
            self.items.append(item_uno)

        if self.tiempo % 12 == 0:
            item_dos = Item((30,30), (300, 450),0, 10, "Recursos/Obstaculos/hamburguesa.png")
            self.items.append(item_dos)

    # CORREGIR ESTA FUNCION
    def posicionar_plataformas(self, rect_pantalla) -> None:

        for plataforma in self.plataformas:
            plataforma.update(rect_pantalla)

    def posicionar_jugador(self, rect_pantalla, jugador, keys) -> None:

        jugador.update(rect_pantalla, self.plataformas, self.enemigos, self.items, keys)

        for proyectil in jugador.lista_proyectiles:
            if proyectil.colisiono:
                jugador.lista_proyectiles.remove(proyectil)
                del proyectil


    #CORREGIR ESTA FUNCION
    def posicionar_enemigos(self, rect_pantalla, jugador) -> None:

        lista = [jugador]
        for enemigo in self.enemigos:
            enemigo.update(rect_pantalla, self.plataformas, lista)
            for proyectil in enemigo.lista_proyectiles:
                if proyectil.colisiono:
                    enemigo.lista_proyectiles.remove(proyectil)
                    del proyectil
            if enemigo.vidas < 0:
                jugador.puntos += enemigo.aporte_puntos
                self.enemigos.remove(enemigo)
                del enemigo

    def posicionar_items(self, rect_pantalla) -> None:

        items_aux = self.items

        for item in self.items:
            item.update(rect_pantalla)
            if item.colisiono:
                items_aux.remove(item)
                del item


    def update(self, rect_pantalla, jugador, keys) -> None:

        rect_pantalla.blit(self.fondo, (0, 0))

        self.posicionar_plataformas(rect_pantalla)
        self.posicionar_enemigos(rect_pantalla, jugador)
        self.posicionar_items(rect_pantalla)
        self.posicionar_jugador(rect_pantalla,jugador, keys)


    def update_personalizado(self, jugador,pantalla, keys):

        self.generar_proyectiles()
        self.generar_enemigos()
        self.generar_items_especiales()
        jugador.update_personalizado(self.enemigos, pantalla, keys)
