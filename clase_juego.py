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
from API_FORMS.GUI_form_estado_juego import CELESTE
from API_FORMS.GUI_form_pausa import FormPausa
from config_db import actualizar_jugador
from datos_juego import W
from modo import *

class Juego():

    def __init__(self, jugador, nivel_actual, base_datos, usuario, niveles:list) -> None:

        self.usuario = usuario
        self.base_datos = base_datos
        self.jugador = jugador
        self.nivel_actual = nivel_actual
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
                if self.jugador.puntos > self.usuario['puntos']: # actualizo solo si los puntos q obtuvo son mayores a los que ya tenia
                    actualizar_jugador(self.nivel_actual, self.jugador.puntos,
                                   self.usuario['usuario'], self.base_datos)
                    print("PUNTOS ANTERIORES: ", self.usuario['puntos'])
                    print("PUNTOS ACTUALES: ", self.jugador.puntos)
                    print("ACTUALIZA LOS PUNTOS")
                self.cerrar_juego()

        if (self.niveles[self.nivel_actual].tiempo <= 0 and
            self.jugador.puntos < self.niveles[self.nivel_actual].puntos_requeridos):

            if self.usuario['nivel_max'] < self.nivel_actual:
                print("PASO A UN NIVEL MAYOR QUE ANTES")
                if self.usuario['puntos'] == 0:# significa que nunca ganó
                    actualizar_jugador(self.nivel_actual, 0, self.usuario['usuario'],
                                       self.base_datos)
                print("GUARDO NIVEL")
                    

            print("NO ALCANZO LOS PUNTOS DEL NIVEL: ", self.nivel_actual)
            self.cerrar_juego()

    def verificar_vida_jugador(self) -> None:

        if self.jugador.vidas <= 0:
            print("MUERTO")
            if self.usuario['nivel_max'] < self.nivel_actual:
                print("PASO A UN NIVEL MAYOR QUE ANTES")
                if self.usuario['puntos'] == 0: # significa que nunca ganó
                    actualizar_jugador(self.nivel_actual, 0, self.usuario['usuario'],
                                       self.base_datos)
                print("GUARDO NIVEL")
            self.cerrar_juego()

    def pausar_juego(self, pantalla) -> None:
        
        # pygame.mixer.music.pause()
        paused = True

        form_pausa = FormPausa(pantalla,
                                   x=W/2-400,
                                   y=25,
                                   w=800,
                                   h=500,
                                   color_background=CELESTE,
                                   color_border="White",
                                   border_size=-1,
                                   active=True,
                                   path_img="Recursos/Interfaces/interfaces_3.png")

        while paused:
            eventos = pygame.event.get()
            pantalla.fill("BLACK")
            form_pausa.update(eventos)

            for event in eventos:
                if event.type == pygame.QUIT:
                    paused = False
                    self.cerrar_juego()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        change_mode()
                    if event.key == pygame.K_x:
                        paused = False
                        # pygame.mixer.music.unpause()


            pygame.display.flip()
   
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
