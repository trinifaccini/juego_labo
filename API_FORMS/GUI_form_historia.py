import pygame
from API_FORMS.GUI_button import Button

from API_FORMS.GUI_form import Form
from API_FORMS.GUI_form_estado_juego import CELESTE
from API_FORMS.GUI_label import Label
from API_FORMS.GUI_button_image import Button_Image
from API_FORMS.GUI_picture_box import PictureBox
from datos_juego import W

class FormHistoria(Form):

    def __init__(self, screen,x,y,w,h, color_background, color_border, border_size,
                 active, path_img):

        super().__init__(screen, x,y, w,h,color_background, color_border, border_size, active)

        # CABECERAS

        self.label = Label(screen=self._slave,
                           x=0,
                           y=0,
                           w=w,
                           h=50,
                           text="HISTORIA DEL JUEGO",
                           font= "Recursos/Fonts/Snowes.ttf",
                           font_size=35,
                           font_color="White",
                           path_image="Recursos/bar.png")
        
        self.label_vidas = Label(screen=self._slave,
                           x=100,
                           y=70,
                           w=220,
                           h=50,
                           text="REPRESENTA LA VIDAS DEL JUGADOR",
                           font= "Recursos/Fonts/Snowes.ttf",
                           font_size=25,
                           font_color="White")



        self.boton_atras = Button_Image(self._slave,
                                           x, y, w-50, h-50,
                                           50, 50,
                                           "Recursos/Interfaces/flecha.png",
                                           self.btn_back_click, "x")
        ######

        self.lista_widgets.append(self.label)
        self.lista_widgets.append(self.label_vidas)
        self.lista_widgets.append(self.boton_atras)
       

    def btn_back_click(self, param) -> None:
        self.end_dialog()

    def render(self):
        self._slave.fill(self._color_background)

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
