import pygame
from pygame.locals import * 

from API_FORMS.GUI_form import Form
from API_FORMS.GUI_button import Button
from API_FORMS.GUI_label import Label
from API_FORMS.GUI_slider import Slider
from API_FORMS.GUI_button_image import Button_Image

CELESTE = (64, 207, 255)

class FormSettings(Form):

    def __init__(self,screen,x,y,w,h,color_background, color_border, border_size, active, path_image):

        super().__init__(screen, x,y, w,h,color_background, color_border, border_size, active)

        # aux_image = pygame.image.load(path_image)
        # aux_image = pygame.transform.scale(aux_image,(w,h))
        # self._slave = aux_image

        pygame.mixer.init()

        ######

        alto_label = 40
        ancho_txt = 200
        alto_txt = 35

        pos_x = w/2 - 250
        pos_x_txt_dos = (w/4)*3 - ancho_txt/2

        y_uno = 90
        espacio = 15


        self.label_settings = Label(self._slave, pos_x, 10, 500, 50,
                                   "CONFIGURACION", "Recursos/Fonts/Snowes.ttf", 40, "White",
                                   "Recursos/Interfaces/interfaces_2.png")

        self.boton_silenciar_audio = Button(self._slave, x, y,
                                 pos_x_txt_dos,  y_uno + alto_txt + alto_label + espacio*2,
                                 ancho_txt, 50,CELESTE, "Blue", self.btn_play_click,
                                 "Nombre", "JUGAR", "Recursos/Fonts/Snowes.ttf", 20, "Black")

        self.boton_play = Button(self._slave, x, y,
                                 300, 50, 100, 50,
                                 "Red", "Blue", self.btn_play_click,
                                 "Nombre", "PAUSE", "Recursos/Fonts/Snowes.ttf", 20, "Black")


        self.label_volumen = Label(self._slave, 700, 100, 100, 30,"20%", 
                                   "Recursos/Fonts/Snowes.ttf", 12, "White", "Recursos/Table.png")

        self.slider_volumen = Slider(self._slave, x,y, 300, 200, 500, 15,
                                     0.2, "Blue", "White")

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
                                        font_size= 25,
                                        font_color= (0,255,0),
                                        path_image="Recursos/home.png"
                                        )


        ######

        self.lista_widgets.append(self.label_settings)
        self.lista_widgets.append(self.boton_silenciar_audio)
        self.lista_widgets.append(self.boton_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.boton_home)

        # pygame.mixer.music.load("Recursos/Audio/musica.mp3")
        # pygame.mixer.music.play(-1) # bucle

        self.render()

    def btn_play_click(self, param):

        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

        else:
            pygame.mixer.music.unpause()

    def update_volumen(self, lista_eventos):

        self.label_volumen.set_text(f"{round(self.slider_volumen.value*100)}%")
        pygame.mixer.music.set_volume(self.slider_volumen.value)

    def btn_home_click(self, param) -> None:

        self.end_dialog()

    def render(self):

        self._slave.fill(self._color_background)

        if pygame.mixer.music.get_busy():
            self.boton_play._color_background = "Red"
            self.boton_play.set_text("PAUSAR")
        else:
            self.boton_play._color_background = "Cyan"
            self.boton_play.set_text("PLAY")


    def update(self, lista_eventos):

        if self.active:
            self.draw()
            self.render()

            for widget in self.lista_widgets:
                widget.update(lista_eventos)

            self.update_volumen(lista_eventos)

        return super().update(lista_eventos)
