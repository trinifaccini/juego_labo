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
from API_FORMS.GUI_button_image import Button_Image
from API_FORMS.GUI_form_estado_juego import CELESTE
from API_FORMS.GUI_form_inicio import TRANSPARENTE
from API_FORMS.GUI_form_pausa import FormPausa
from API_FORMS.GUI_form_settings import FormSettings
from config_db import actualizar_jugador
from datos_juego import W
from modo import *
from datos_nivel_uno import nivel_uno
from datos_nivel_dos import nivel_dos
from datos_nivel_tres import nivel_tres

class Juego():

    def __init__(self, pantalla, jugador, nivel_actual, base_datos, usuario) -> None:

        self.pantalla = pantalla
        self.usuario = usuario
        self.jugando = True
        self.base_datos = base_datos
        self.jugador = jugador
        self.nivel_actual = nivel_actual

        # uno = Nivel(nivel_uno['fondo'], nivel_uno['plat'], nivel_uno['enemigos'],
        #             nivel_uno['items'], nivel_uno['tiempo'], nivel_uno['puntos'], 1,
        #             nivel_uno['temp'])
        
        # dos = Nivel(nivel_dos['fondo'], nivel_dos['plat'], nivel_dos['enemigos'],
        #             nivel_dos['items'], nivel_dos['tiempo'], nivel_dos['puntos'], 1,
        #             nivel_dos['temp'])
        
        # tres = Nivel(nivel_tres['fondo'], nivel_tres['plat'], nivel_tres['enemigos'],
        #             nivel_tres['items'], nivel_tres['tiempo'], nivel_tres['puntos'], 1,
        #             nivel_tres['temp'])

        self.niveles = [nivel_uno, nivel_dos, nivel_tres]
        self.estado_juego = None

        self.boton_config = Button_Image(pantalla, 0, 0,W-60,70,50,50,
                                 "Recursos/Interfaces/button_settings.png",
                                 self.btn_config_click, "x")

        self.boton_pausa = Button_Image(pantalla, 0, 0,W-60,130,50,50,
                                 "Recursos/Interfaces/button_pause.png",
                                 self.btn_pausar_click, "x")
        
        self.boton_audio = Button_Image(pantalla, 0, 0,W-60,190,50,50,
                                 "Recursos/Interfaces/button_sound.png",
                                 self.btn_sonido_click, "x")


    def generar_posicionar_textos(self, pantalla, fuente) -> None:

        texto = fuente.render(f"Vidas: {self.jugador.vidas}", False, CELESTE, "Blue")
        ancho_texto = texto.get_width()

        texto_vidas = {
            "texto": texto,
            "pos_x": pantalla.get_width()-ancho_texto-10,
            "pos_y": 2
        }

        texto = fuente.render(f"Puntos: {self.jugador.puntos}", False,CELESTE, "Blue")

        texto_puntos = {
            "texto": texto,
            "pos_x": 10,
            "pos_y": 2
        }

        texto = fuente.render(f"TIEMPO RESTANTE: {self.niveles[self.nivel_actual].tiempo}",
                              False, CELESTE, "Blue")
        
        ancho_texto = texto.get_width()

        texto_tiempo = {
            "texto": texto,
            "pos_x": pantalla.get_width()/2-(ancho_texto/2),
            "pos_y": 2
        }

        textos = [texto_vidas, texto_puntos, texto_tiempo]

        for texto in textos:
            pantalla.blit(texto['texto'], (texto['pos_x'], texto['pos_y']))

    def btn_pausar_click(self, param):

        form_pausa = FormPausa(self.pantalla,
                                        x=W/2-300,
                                        y=25,
                                        w=600,
                                        h=500,
                                        color_background=TRANSPARENTE,
                                        color_border="White",
                                        border_size=-1,
                                        active=True,
                                        path_img="Recursos/Interfaces/interfaces_3.png")
        
        self.pausar_juego(form_pausa)

    def btn_config_click(self, param):

        form_settings = FormSettings(self.pantalla,
                                   x=W/2-400,
                                   y=25,
                                   w=800,
                                   h=500,
                                   color_background=TRANSPARENTE,
                                   color_border="White",
                                   border_size=-1,
                                   active=True,
                                   path_image="")

        self.pausar_juego(form_settings)

    def btn_sonido_click(self, param):
        
        if self.jugador.volumen == 0:
            self.boton_audio.set_background_image("Recursos/Interfaces/button_sound.png")
            self.jugador.volumen = 5

        else:
            self.boton_audio.set_background_image("Recursos/Interfaces/button_nosound.png")
            self.jugador.volumen = 0


    def posicionar_form_general(self, lista_eventos) -> None:
        self.boton_config.update(lista_eventos)
        self.boton_pausa.update(lista_eventos)
        self.boton_audio.update(lista_eventos)

    def cerrar_juego(self):

        pygame.quit()
        sys.exit(0)

    def verificar_puntos_tiempo(self) -> None:

        if self.jugador.puntos >= self.niveles[self.nivel_actual].puntos_requeridos:

            if self.nivel_actual < len(self.niveles)-1:
                self.jugador.puntos += (self.niveles[self.nivel_actual].tiempo * 100)
                self.nivel_actual += 1
            else:
                if self.jugador.puntos > self.usuario['puntos']: # actualizo solo si los puntos q obtuvo son mayores a los que ya tenia
                    actualizar_jugador(self.nivel_actual, self.jugador.puntos,
                                   self.usuario['usuario'], self.base_datos)
                self.estado_juego = "gano"

        if (self.niveles[self.nivel_actual].tiempo <= 0 and
            self.jugador.puntos < self.niveles[self.nivel_actual].puntos_requeridos):

            if self.usuario['nivel_max'] < self.nivel_actual:
 
                if self.usuario['puntos'] == 0:# significa que nunca ganó
                    actualizar_jugador(self.nivel_actual, 0, self.usuario['usuario'],
                                       self.base_datos)
  
            self.estado_juego = "perdio"
        
    def verificar_vida_jugador(self) -> None:

        if self.jugador.vidas <= 0:
            if self.usuario['nivel_max'] < self.nivel_actual:
                if self.usuario['puntos'] == 0: # significa que nunca ganó
                    actualizar_jugador(self.nivel_actual, 0, self.usuario['usuario'],
                                       self.base_datos)
            self.estado_juego = "murio"

    def pausar_juego(self, formulario) -> None:

        while formulario.pausado:
            eventos = pygame.event.get()
            self.pantalla.fill("BLACK")
            formulario.update(eventos)
            if formulario.jugando is False:
                #paused = False
                self.jugando = False
            for event in eventos:
                if event.type == pygame.QUIT:
                    self.cerrar_juego()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        change_mode()
                    # if event.key == pygame.K_x:
                    #     paused = False
                        # pygame.mixer.music.unpause()

            pygame.display.flip()

    def manejar_eventos_juego(self, pantalla, eventos):

        for evento in eventos:

            if evento.type == pygame.QUIT:
                self.cerrar_juego()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    change_mode()
                # if evento.key == pygame.K_x:
                #     self.pausar_juego()

    def reiniciar_enemigos_niveles(self) -> None:
        for nivel in self.niveles:
            nivel.resetear_enemigos_nivel()

    def reiniciar_juego(self) -> None:
        self.niveles[self.nivel_actual].tiempo = 60
        self.jugador.vidas = 1100
        self.reiniciar_enemigos_niveles()


    def update(self, pantalla,fuente, eventos, keys) -> None:

        self.verificar_puntos_tiempo()
        self.verificar_vida_jugador()

        self.niveles[self.nivel_actual].update(pantalla, self.jugador, keys)
        self.generar_posicionar_textos(pantalla, fuente)
        self.posicionar_form_general(eventos)

    def update_personalizado(self, pantalla, keys) -> None:

        self.niveles[self.nivel_actual].update_personalizado(self.jugador,pantalla, keys)
