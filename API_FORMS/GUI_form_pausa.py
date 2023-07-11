import pygame

from API_FORMS.GUI_form import Form
from API_FORMS.GUI_form_inicio import TRANSPARENTE
from API_FORMS.GUI_form_reglas import FormReglas
from API_FORMS.GUI_form_settings import FormSettings
from API_FORMS.GUI_label import Label
from API_FORMS.GUI_button_image import Button_Image
from datos_juego import H, W

class FormPausa(Form):

    def __init__(self, screen,x,y,w,h, color_background, color_border, border_size,
                 active, path_img):

        super().__init__(screen, x,y, w,h,color_background, color_border, border_size, active)

        aux_imagen = pygame.image.load(path_img)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))

        self._slave = aux_imagen
        self.jugando = True
        self.pausado = True
        self.estado_musica = pygame.mixer.music.get_busy()
        print(self.estado_musica)

        pygame.mixer.music.pause()

        ancho_btn = 50

        # CABECERAS

        self.label = Label(screen=self._slave,
                           x=0,
                           y=100,
                           w=w,
                           h=50,
                           text="JUEGO PAUSADO",
                           font= "Recursos/Fonts/Snowes.ttf",
                           font_size=35,
                           font_color="White",
                           path_image="Recursos/bar.png")


        self.boton_atras = Button_Image(self._slave,
                                           x, y, 0, h/2,
                                           ancho_btn, ancho_btn,
                                           "Recursos/Interfaces/flecha.png",
                                           self.btn_back_click, "x"
                                        )


        self.boton_home = Button_Image(self._slave,
                                         x, y, w-ancho_btn, h/2,
                                         ancho_btn, ancho_btn,
                                         "Recursos/Interfaces/home.png",
                                          self.btn_home_click, "x"
                                        )
        
        self.boton_reglas = Button_Image(self._slave, x, y,
                                 w/2-ancho_btn/2, h/2,
                                 ancho_btn, ancho_btn,
                                 "Recursos/Interfaces/button_info.png",
                                 self.btn_info_click, "x")

        ######

        self.lista_widgets.append(self.label)
        self.lista_widgets.append(self.boton_home)
        self.lista_widgets.append(self.boton_atras)
        self.lista_widgets.append(self.boton_reglas)

    def btn_home_click(self, param) -> None:

        pygame.mixer.init()

        self.jugando = False
        self.pausado = False
        pygame.mixer.music.load("Recursos/Audio/fondo.mp3")
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume())
        pygame.mixer.music.play(-1) # bucle
        self.end_dialog()

    def btn_back_click(self, param) -> None:
        self.pausado = False

        if self.estado_musica is True:
            pygame.mixer.music.unpause()

        self.end_dialog()

    def btn_info_click(self, param):

        form_info = FormReglas(self._master,
                                x=W/2-((W-200)/2),
                                y=50,
                                w=W-200,
                                h=H-100,
                                color_background=TRANSPARENTE,
                                color_border="White",
                                border_size=-1,
                                active=True,
                                path_img="Recursos/Interfaces/interfaces_3.png")

        self.show_dialog(form_info)
        

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
