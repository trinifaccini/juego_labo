# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=too-many-arguments

'''
ARCHIVO CLASE NIVEL
'''

import copy
import random
from clase_boss import deepcopy_boss
from clase_enemigo import Enemigo, deepcopy_enemigo
from clase_item import Item, deepcopy_item
from config_img import *
from datos_juego import H, W

class Nivel():

    def __init__(self, fondo, plataformas:list, enemigos_iniciales:list,
                 items_iniciales:list, trampas, tiempo:int, enemigos_requeridos:int, max_enemigos:int,
                 nivel:int, temporizador) -> None:

        self.fondo = fondo
        self.tiempo = tiempo
        self.enemigos_iniciales = enemigos_iniciales
        self.items_iniciales = items_iniciales
        self.max_enemigos = max_enemigos

        enemigos = []
        for enemigo in enemigos_iniciales:
            enemigos.append(deepcopy_enemigo(enemigo))

        items = []
        for item in items_iniciales:
            items.append(deepcopy_item(item))

        self.enemigos = enemigos
        self.items = items
        self.trampas = trampas
        self.plataformas = plataformas # las plataformas van a venir con las trampas
        self.nivel = nivel
        self.enemigos_requeridos = enemigos_requeridos
        self.enemigos_muertos = 0
        self.temporizador = temporizador

    def copiar(self):
        return copy.deepcopy(self)

    def generar_proyectiles(self) -> None:

        for enemigo in self.enemigos:
            if self.tiempo % enemigo.temporizador == 0 and enemigo.accion != "ataca":
                enemigo.lanzar_proyectil(15)

    def enemigo_segun_nivel(self) -> Enemigo:

        temporizador = random.randint(3, 10)
        lista_pos_x = []

        for plat in self.plataformas:
            if plat.lados['main'].width >= 200:
                lista_pos_x.append(plat.lados['main'].x)

        rand = random.randint(0, len(lista_pos_x)-1)

        if self.nivel == 1:
            return Enemigo((70,60), (lista_pos_x[rand],0), diccionario_animaciones_oso_normal,
                                diccionario_animaciones_oso_rojo,  3, -15,150,100,100, temporizador)

        if self.nivel == 2:
            return Enemigo((80,70), (lista_pos_x[rand],0), diccionario_animaciones_yeti_normal,
                            diccionario_animaciones_yeti_rojo, 5, -15, 450,150,200,temporizador)

    def generar_enemigos(self) -> None:

        if self.tiempo % self.temporizador == 0 and self.nivel != 3:

            if len(self.enemigos) < self.max_enemigos:
                enemigo = self.enemigo_segun_nivel()
                self.enemigos.append(enemigo)

    def generar_items_especiales(self) -> None:

        if self.tiempo % 10 == 0:
            pos_x = random.randint(0, W-100)
            pos_y = random.randint(200, H-80)
            item_uno = Item((30,50), (pos_x, pos_y), 10, 0, "Recursos/Obstaculos/coca.png")
            self.items.append(item_uno)

        if self.tiempo % 15 == 0:
            pos_x = random.randint(0, W-100)
            pos_y = random.randint(200, H-40)
            item_dos = Item((30,30), (300, 450),0, 10, "Recursos/Obstaculos/hamburguesa.png")
            self.items.append(item_dos)

    # CORREGIR ESTA FUNCION
    def posicionar_plataformas(self, rect_pantalla) -> None:

        for plataforma in self.plataformas:
            plataforma.update(rect_pantalla)

    def posicionar_jugador(self, rect_pantalla, jugador, keys) -> None:

        jugador.update(rect_pantalla, self.plataformas, self.enemigos, self.items,
                       self.trampas, keys)

        for proyectil in jugador.lista_proyectiles:
            if proyectil.colisiono:
                jugador.lista_proyectiles.remove(proyectil)
                del proyectil


    #CORREGIR ESTA FUNCION
    def posicionar_enemigos(self, rect_pantalla, jugador) -> None:

        lista = [jugador]
        
        for enemigo in self.enemigos:

            if self.nivel == 3:
                enemigo.update(rect_pantalla, self.plataformas, self.items, lista, self.tiempo)
            else:
                enemigo.update(rect_pantalla, self.plataformas, lista, self.tiempo)
            for proyectil in enemigo.lista_proyectiles:
                if proyectil.colisiono:
                    enemigo.lista_proyectiles.remove(proyectil)
                    del proyectil
            if enemigo.vidas < 0:
                jugador.puntos += enemigo.aporte_puntos
                self.enemigos.remove(enemigo)
                self.enemigos_muertos += 1
                del enemigo

    def posicionar_items(self, rect_pantalla) -> None:

        items_aux = self.items

        for item in self.items:
            item.update(rect_pantalla)
            if item.colisiono:
                items_aux.remove(item)
                del item

    def posicionar_trampas(self, rect_pantalla) -> None:

        for trampa in self.trampas:
            trampa.update(rect_pantalla)


    def update(self, rect_pantalla, jugador, keys) -> None:

        rect_pantalla.blit(self.fondo, (0, 0))

        self.posicionar_plataformas(rect_pantalla)
        self.posicionar_enemigos(rect_pantalla, jugador)
        self.posicionar_items(rect_pantalla)
        self.posicionar_trampas(rect_pantalla)
        self.posicionar_jugador(rect_pantalla,jugador, keys)

    def resetear_enemigos_nivel(self) -> None:

        self.enemigos.clear()
        enemigos = []

        if self.nivel != 3:
            for enemigo in self.enemigos_iniciales:
                enemigos.append(deepcopy_enemigo(enemigo))
        else:
            enemigos.append(deepcopy_boss(self.enemigos_iniciales[0]))

        self.enemigos = enemigos

    def resetear_items_nivel(self) -> None:

        self.items.clear()
        items = []

        for item in self.items_iniciales:
            items.append(deepcopy_item(item))

        self.items = items


    def update_personalizado(self, jugador,pantalla, keys):

        self.generar_proyectiles()
        self.generar_enemigos()
        self.generar_items_especiales()
        jugador.update_personalizado(self.enemigos, self.trampas, pantalla, keys)
