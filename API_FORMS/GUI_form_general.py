import pygame
from pygame.locals import * 

from API_FORMS.GUI_form import Form
from API_FORMS.GUI_form_settings import FormSettings
from API_FORMS.GUI_label import Label
from API_FORMS.GUI_button_image import Button_Image
from datos_juego import W

class FormGeneral(Form):

    def __init__(self, screen,x,y,w,h, color_background, color_border, border_size,active):

        super().__init__(screen, x,y, w,h,color_background, color_border, border_size, active)

        ancho_btn_ranking = 50

        # CABECERAS

        self.label = Label(screen=self._slave,
                           x=100,
                           y=100,
                           w=600,
                           h=50,
                           text="PRESIONA X PARA REANUDAR",
                           font= "Recursos/Fonts/Snowes.ttf",
                           font_size=25,
                           font_color="White",
                           path_image="Recursos/bar.png")

        self.boton_settings = Button_Image(self._slave, x, y,
                                 w/2 - ancho_btn_ranking/2, 400,
                                 ancho_btn_ranking, ancho_btn_ranking,
                                 "Recursos/Menu_BTN.png",
                                 self.btn_settings_click, "x")

        ######

        self.lista_widgets.append(self.label)
        self.lista_widgets.append(self.boton_settings)


    def btn_settings_click(self, param) -> None:

        form_settings = FormSettings(self._master,
                                   x=W/2-400,
                                   y=25,
                                   w=800,
                                   h=500,
                                   color_background=(220,0,220),
                                   color_border="White",
                                   border_size=-1,
                                   active=True,
                                   path_image="")

        self.show_dialog(form_settings)

    def render(self):
        self.draw()

    def update(self, lista_eventos):

        if self.verificar_dialog_result():
 
            if self.active:
                self.render()

                for widget in self.lista_widgets:
                    widget.update(lista_eventos)

                # self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

        return super().update(lista_eventos)
