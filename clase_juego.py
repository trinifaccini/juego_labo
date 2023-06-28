'''
CLASE JUEGO
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
# pylint: disable=arguments-differ
# pylint: disable=no-member

import sys
import pygame
from API_FORMS.GUI_form_ranking import FormRanking
from config_db import actualizar_jugador, traer_ranking_db
from modo import *

class Juego():

    def __init__(self, jugador, base_datos, usuario, niveles:list) -> None:

        self.usuario = usuario
        self.base_datos = base_datos
        self.jugador = jugador
        self.nivel_actual = 0
        self.niveles = niveles

    def posicionar_textos(self, pantalla, textos) -> None:

        for texto in textos:
            pantalla.blit(texto['texto'], (texto['pos_x'], texto['pos_y']))

    def cerrar_juego(self):

        pygame.quit()
        sys.exit(0)

    def verificar_puntos_tiempo(self) -> None:

        if self.jugador.puntos >= self.niveles[self.nivel_actual].puntos_requeridos:

            if self.nivel_actual < len(self.niveles)-1:
                print("PASO DE NIVEL")
                self.jugador.puntos += (self.niveles[self.nivel_actual].tiempo * 100)
                self.nivel_actual += 1
            else:
                actualizar_jugador(self.nivel_actual, self.jugador.puntos,
                                   self.usuario, self.base_datos)
                self.cerrar_juego()

        if (self.niveles[self.nivel_actual].tiempo <= 0 and
            self.jugador.puntos < self.niveles[self.nivel_actual].puntos_requeridos):
            actualizar_jugador(self.nivel_actual, 0, self.usuario, self.base_datos)
            print("NO ALCANZO LOS PUNTOS DEL NIVEL: ", self.nivel_actual)
            self.cerrar_juego()

    def verificar_vida_jugador(self) -> None:
        if self.jugador.vidas <= 0:
            print("MUERTO")
            self.cerrar_juego()

    def pausar_juego(self, pantalla) -> None:

        paused = True

        dic_score = traer_ranking_db("jugadores.db")
        
        # LE PASAMOS EL MASTER PORQUE ESTE FORM QUEREMOS QUE SE BLITEE EN RELACION
        # A LA PANTALLA, NO AL FORM DE INICIO

        form_ranking = FormRanking(pantalla,
                                   x=250,
                                   y=25,
                                   w=500,
                                   h=550,
                                   color_background=(220,0,220),
                                   color_border="White",
                                   border_size=5,
                                   active=True,
                                   path_img="Recursos/Window.png",
                                   scores=dic_score,
                                   margen_x=10,
                                   margen_y=100,
                                   espacio=10)

        while paused:
            eventos = pygame.event.get()
            pantalla.fill("Black")
            form_ranking.update(eventos)
            pygame.display.flip()

            for event in eventos:
                if event.type == pygame.QUIT:
                    paused = False
                    self.cerrar_juego()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        change_mode()
                    if event.key == pygame.K_x:
                        paused = False
   
    def manejar_eventos_juego(self, pantalla, eventos):

        for evento in eventos:

            match evento.type:
                case pygame.QUIT:
                    self.cerrar_juego()
                case pygame.KEYDOWN:
                    if evento.key == pygame.K_TAB:
                        change_mode()
                    if evento.key == pygame.K_x:
                        self.pausar_juego(pantalla)

    def update(self, pantalla, fuente, keys) -> None:

        self.verificar_puntos_tiempo()
        self.verificar_vida_jugador()

        self.niveles[self.nivel_actual].update(pantalla, self.jugador, keys)

        texto = fuente.render(f"Vidas: {self.jugador.vidas}", False, "Green", "Blue")
        ancho_texto = texto.get_width()

        texto_vidas = {
            "texto": texto,
            "pos_x": pantalla.get_width()-ancho_texto,
            "pos_y": 0
        }

        texto = fuente.render(f"Puntos: {self.jugador.puntos}", False, "Blue")

        texto_puntos = {
            "texto": texto,
            "pos_x": 0,
            "pos_y": 0
        }

        texto = fuente.render(f"Tiempo:{self.niveles[self.nivel_actual].tiempo}",
                              False, "Green", "Blue")
        ancho_texto = texto.get_width()

        texto_tiempo = {
            "texto": texto,
            "pos_x": pantalla.get_width()/2-(ancho_texto/2),
            "pos_y": 0
        }

        textos = [texto_vidas, texto_puntos, texto_tiempo]

        self.posicionar_textos(pantalla, textos)

    def update_personalizado(self, pantalla, keys) -> None:

        self.niveles[self.nivel_actual].update_personalizado(self.jugador,pantalla, keys)
