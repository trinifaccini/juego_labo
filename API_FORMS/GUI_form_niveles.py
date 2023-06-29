import pygame
from pygame.locals import *
from API_FORMS.GUI_button_image import Button_Image 

from API_FORMS.GUI_form import Form
from API_FORMS.GUI_button import Button
from API_FORMS.GUI_label import Label
from config_db import buscar_usuario_db, insertar_jugador, traer_ranking_db

CELESTE = (64, 207, 255)

class FormNiveles(Form):

    def __init__(self, screen,x,y,w,h, path_image, nivel_max, color_background = None, color_border="Magenta", border_size=-1,
                 active=True):

        super().__init__(screen, x,y, w,h,color_background, color_border, border_size, active)
        ######

        ancho_label = 250
        alto_label = 40


        ancho_nivel = 150

        ancho_txt = 200
        alto_txt = 35

        pos_x_label_uno = (w-ancho_label)/2
        pos_x_niveles = (w - ancho_nivel)/2

        y_uno = 90
        espacio = 20

        self.nivel_max = nivel_max

        self.label_elegir = Label(self._slave, pos_x_label_uno, 10, ancho_label, 50,
                                   "ELEGIR NIVEL", "Recursos/Fonts/Snowes.ttf", 40, "White",
                                   "Recursos/Interfaces/interfaces_2.png")

        pos_inicial_y = y_uno

        for nivel in range(nivel_max+1):

            # label_nivel = Label(self._slave, pos_x_niveles, pos_inicial_y,
            #                             ancho_nivel, alto_label,
            #                             f"NIVEL {nivel+1}", "Recursos/Fonts/Snowes.ttf", 25, 
            #                                  "White", "Recursos/Interfaces/interfaces.png")
            
            boton_nivel = Button_Image(self._slave,
                                        x= pos_x_niveles,
                                        y= pos_inicial_y,
                                        master_x= x,
                                        master_y=y,
                                        w= ancho_nivel,
                                        h=alto_label,
                                        color_background=None,
                                        color_border=(255,0,255),
                                        border_size=-1,
                                        onclick=self.btn_jugar_click,
                                        onclick_param=nivel,
                                        font="Recursos/Fonts/Snowes.ttf",
                                        font_size= 25,
                                        font_color= "White",
                                        path_image="Recursos/Interfaces/interfaces.png",
                                        text=f"NIVEL {nivel+1}"
                                        )

            self.lista_widgets.append(boton_nivel)

            pos_inicial_y += alto_label + espacio

        self.boton_jugar = Button(self._slave, x, y,
                                 pos_x_niveles, y_uno + alto_label*3 + espacio*3,
                                 ancho_nivel, 50,
                                 CELESTE, "Blue", self.btn_jugar_click,
                                 "Nombre", "JUGAR", "Recursos/Fonts/Snowes.ttf", 20, "Black")


        ######

        self.lista_widgets.append(self.label_elegir)
        self.lista_widgets.append(self.boton_jugar)

        self.render()


    def btn_jugar_click(self, param):

        self.padre.nivel = param
        self.padre.flag_jugar = True
        self.end_dialog()

    def render(self):

       self.draw()

    def update(self, lista_eventos):

        # if self.verificar_dialog_result():

        if self.active:
            self.draw()
            self.render()

            for widget in self.lista_widgets:
                widget.update(lista_eventos)

        # else:
        #     self.hijo.update(lista_eventos)

        return super().update(lista_eventos)
