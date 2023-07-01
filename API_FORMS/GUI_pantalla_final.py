import pygame
from pygame.locals import * 

from API_FORMS.GUI_form import Form
from API_FORMS.GUI_button import Button
from API_FORMS.GUI_form_niveles import FormNiveles
from API_FORMS.GUI_form_settings import FormSettings
from API_FORMS.GUI_textbox import TextBox
from API_FORMS.GUI_label import Label
from API_FORMS.GUI_button_image import Button_Image
from API_FORMS.GUI_form_ranking import FormRanking
from config_db import buscar_usuario_db, insertar_jugador, traer_ranking_db
from datos_juego import W

CELESTE = (64, 207, 255)
TRANSPARENTE = (0,0,0,0)


class FormFinal(Form):

    def __init__(self, screen,x,y,w,h, path_image, estado_juego, color_background = None, color_border="Magenta", border_size=-1,
                 active=True):

        super().__init__(screen, x,y, w,h,color_background, color_border, border_size, active)

        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image

        ######

        pos_x = w/2 - 250

        if estado_juego == "gano":
            texto = "GANASTE"
            texto_adicional = "TUS PUNTOS: "
        elif estado_juego == "perdiste":
            texto = "PERDISTE"
            texto_adicional = "NO ALCANZASTE LOS PUNTOS"
        else:
            texto = "PERDISTE"
            texto_adicional = "TE QUEDASTE SIN VIDA"


        self.label_bienvenida = Label(self._slave, pos_x, 10, 500, 50,
                                   texto, "Recursos/Fonts/Snowes.ttf", 40, "White",
                                   "Recursos/Interfaces/interfaces_2.png")
        
        self.label_adicional = Label(self._slave, pos_x, 70, 500, 50,
                                   texto_adicional, "Recursos/Fonts/Snowes.ttf", 40, "White",
                                   "Recursos/Interfaces/interfaces_2.png")



        ######

        self.lista_widgets.append(self.label_bienvenida)
        self.lista_widgets.append(self.label_adicional)
        self.render()


    def render(self):
        self.draw()

    def update(self, lista_eventos):

        if self.verificar_dialog_result():

            if self.active:
                self.draw()
                self.render()

                for widget in self.lista_widgets:
                    widget.update(lista_eventos)

        else:
            self.hijo.update(lista_eventos)

        return super().update(lista_eventos)
