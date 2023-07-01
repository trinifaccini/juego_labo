import pygame
from pygame.locals import * 

from API_FORMS.GUI_form import Form
from API_FORMS.GUI_form_settings import FormSettings
from API_FORMS.GUI_label import Label
from API_FORMS.GUI_button_image import Button_Image
from datos_juego import W

class FormPausa(Form):

    def __init__(self, screen,x,y,w,h, color_background, color_border, border_size,
                 active, path_img):

        super().__init__(screen, x,y, w,h,color_background, color_border, border_size, active)

        aux_imagen = pygame.image.load(path_img)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))

        self._slave = aux_imagen
        self.jugando = True

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
        

        self.boton_home = Button_Image(self._slave,
                                        x= w-70,
                                        y= h-70,
                                        master_x= x,
                                        master_y=y,
                                        w= 50,
                                        h=50,
                                        color_background= (255,0,0),
                                        color_border=(255,0,255),
                                        onclick=self.btn_home_click,
                                        onclick_param="",
                                        font_size= 15,
                                        font_color= (0,255,0),
                                        path_image="Recursos/home.png"
                                        )

        ######

        self.lista_widgets.append(self.label)
        self.lista_widgets.append(self.boton_home)
        self.lista_widgets.append(self.boton_settings)

    def btn_home_click(self, param) -> None:

        self.jugando = False
        print(self.jugando)
        self.end_dialog()

    def btn_settings_click(self, param) -> None:

        form_settings = FormSettings(self._master,
                                   x=W/2-400,
                                   y=25,
                                   w=800,
                                   h=500,
                                   color_background="Black",
                                   color_border="White",
                                   border_size=-1,
                                   active=True,
                                   path_image="")

        self.show_dialog(form_settings)

    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):

        if self.verificar_dialog_result():
 
            if self.active:
                self.draw()
                self.render()

                for widget in self.lista_widgets:
                    widget.update(lista_eventos)

                # self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

        return super().update(lista_eventos)
