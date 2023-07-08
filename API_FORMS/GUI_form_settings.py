import pygame
from pygame.locals import * 

from API_FORMS.GUI_form import Form
from API_FORMS.GUI_button import Button
from API_FORMS.GUI_label import Label
from API_FORMS.GUI_slider import Slider
from API_FORMS.GUI_button_image import Button_Image

CELESTE = (64, 207, 255)

class FormSettings(Form):

    def __init__(self,screen,x,y,w,h,color_background, color_border, border_size,
                 active, path_image):

        super().__init__(screen, x,y, w,h,color_background, color_border, border_size, active)

        # aux_image = pygame.image.load(path_image)
        # aux_image = pygame.transform.scale(aux_image,(w,h))
        # self._slave = aux_image

        pygame.mixer.init()

        ancho_txt = 200

        pos_x = w/2 - 250
        pos_x_txt_dos = w/2 - ancho_txt/2

        ancho_slider = 500
        pos_x_slider = w/2 - ancho_slider/2

        ancho_label_volumen = 80
        pos_x_label_volumen = w/2 - ancho_label_volumen/2

        self.jugando = True
        self.pausado = True
        self.sonido_silenciado = False

        self.label_settings = Label(self._slave, pos_x, 10, 500, 50,
                                   "CONFIGURACION", "Recursos/Fonts/Snowes.ttf", 40, "White",
                                   "Recursos/Interfaces/interfaces_2.png")

        self.label_volumen = Label(self._slave, pos_x_txt_dos, 60, ancho_txt, 80,"VOLUMEN MUSICA",
                                   "Recursos/Fonts/Snowes.ttf", 40, "White", "")

        self.label_porcentaje_volumen = Label(self._slave, pos_x_label_volumen, 150, 80, 80,"20%",
                                   "Recursos/Fonts/Snowes.ttf", 40, "White",
                                   "Recursos/Interfaces/interfaces_4.png")

        self.slider_volumen = Slider(self._slave, x,y, pos_x_slider, 250, ancho_slider, 15,
                                     pygame.mixer.music.get_volume(), "Blue", "White")

        if pygame.mixer.music.get_busy():
            texto_musica = "SILENCIAR MUSICA"
        else:
            texto_musica = "REANUDAR MUSICA"

        self.boton_musica = Button(self._slave, x, y,
                                 w/2-ancho_txt/2, 300,
                                 ancho_txt, 50,CELESTE, "Blue", self.btn_play_click, "x",
                                 texto_musica, "Recursos/Fonts/Snowes.ttf", 30, "Black")

        # self.boton_sonidos = Button(self._slave, x, y,
        #                          w/2+5, 300,
        #                          ancho_txt, 50,CELESTE, "Blue", self.btn_sonidos_click, "x",
        #                          "SILENCIAR AUDIO", "Recursos/Fonts/Snowes.ttf", 30, "Black")

        self.boton_atras = Button_Image(self._slave,
                                        x= w-70,
                                        y= h-70,
                                        master_x= x,
                                        master_y=y,
                                        w= 50,
                                        h=50,
                                        color_background= (255,0,0),
                                        color_border=(255,0,255),
                                        onclick=self.btn_back_click,
                                        onclick_param="",
                                        font_size= 25,
                                        font_color= (0,255,0),
                                        path_image="Recursos/Interfaces/flecha.png"
                                        )


        ######

        self.lista_widgets.append(self.label_settings)
        self.lista_widgets.append(self.boton_musica)
        #self.lista_widgets.append(self.boton_sonidos)
        self.lista_widgets.append(self.label_porcentaje_volumen)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.boton_atras)

        # pygame.mixer.music.load("Recursos/Audio/musica.mp3")
        # pygame.mixer.music.play(-1) # bucle

        self.render()

    def btn_play_click(self, param):

        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.boton_musica.set_text("REANUDAR MUSICA")
            pygame.mixer.music.pause()

        else:
            pygame.mixer.music.unpause()
            self.boton_musica.set_text("SILENCIAR MUSICA")

    # def btn_sonidos_click(self, param):

    #     if self.sonido_silenciado is False:
    #         self.sonido_silenciado = True
    #         self.boton_sonidos.set_text("REANUDAR AUDIO")
    #         pygame.mixer.music.pause()

    #     else:
    #         self.sonido_silenciado = False
    #         self.boton_sonidos.set_text("SILENCIAR AUDIO")

    def update_volumen(self, lista_eventos):

        self.label_porcentaje_volumen.set_text(f"{round(self.slider_volumen.value*100)}%")
        pygame.mixer.music.set_volume(self.slider_volumen.value)

    def btn_back_click(self, param) -> None:
        self.pausado = False
        self.end_dialog()

    def render(self):

        self._slave.fill(self._color_background)

    def update(self, lista_eventos):

        if self.active:
            self.draw()
            self.render()

            for widget in self.lista_widgets:
                widget.update(lista_eventos)

            self.update_volumen(lista_eventos)

        return super().update(lista_eventos)
