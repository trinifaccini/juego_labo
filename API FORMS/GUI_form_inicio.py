import pygame
from pygame.locals import * 

from GUI_form import Form
from GUI_button import Button
from GUI_textbox import TextBox
from GUI_label import Label
from GUI_slider import Slider
from GUI_button_image import Button_Image
from GUI_form_ranking import FormRanking

class FormInicio(Form):

    def __init__(self, screen,x,y,w,h,color_background, color_border="black", border_size=-1,
                 active=True):

        super().__init__(screen, x,y, w,h,color_background, color_border, border_size, active)

        self.volumen = 0.2
        self.flag_play = True

        pygame.mixer.init()

        ######

        self.nombre_jugador = TextBox(self._slave, x,x,
                                      50, 50, 150,30,
                                      "Blue", "White", "Red", "Pink", 5,
                                      "Arial", 12, "Black")

        self.apellido_jugador = TextBox(self._slave, x,x,
                                        50, 150,150,30,
                                        "Blue", "White", "Red", "Pink", 5,
                                        "Arial", 12, "Black")

        self.usuario_jugador = TextBox(self._slave, x, y,
                                       50, 250,150,30,
                                       "Blue", "White", "Red", "Pink", 5,
                                       "Arial", 12, "Black")

        self.boton_play = Button(self._slave, x, y,
                                 300, 50, 100, 50,
                                 "Red", "Blue", self.btn_play_click,
                                 "Nombre", "PAUSE", "Arial", 12, "Black")

        self.label_volumen = Label(self._slave, 700, 100, 100, 30,
                                   "20%", "Arial", 12, "White", "Recursos/Table.png")

        self.slider_volumen = Slider(self._slave, x,y, 300, 200, 500, 15,
                                     self.volumen, "Blue", "White")

        self.boton_ranking = Button_Image(self._slave, x, y,
                                 600, 50, 50, 50,
                                 "Recursos/Menu_BTN.png",
                                 self.btn_ranking_click, "x")
        ######

        self.lista_widgets.append(self.nombre_jugador)
        self.lista_widgets.append(self.apellido_jugador)
        self.lista_widgets.append(self.usuario_jugador)
        self.lista_widgets.append(self.boton_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.boton_ranking)

        pygame.mixer.music.load("Recursos/Audio/musica.mp3")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1) # bucle

        self.render()

    def btn_play_click(self, param):

        #print(self.nombre_jugador.get_text())

        if self.flag_play:
            pygame.mixer.music.pause()
            self.boton_play._color_background = "Cyan"
            self.boton_play.set_text("PLAY")

        else:
            pygame.mixer.music.unpause()
            self.boton_play._color_background = "Red"
            self.boton_play.set_text("PAUSE")

        self.flag_play = not self.flag_play


    def btn_ranking_click(self, param):

        #print(self.nombre_jugador.get_text())

        dic_score = [{"Usuario": "trinif", "Puntos": 1000},
                     {"Usuario": "trinif", "Puntos": 2000},
                     {"Usuario": "trinif", "Puntos": 3000}]
        
        # LE PASAMOS EL MASTER PORQUE ESTE FORM QUEREMOS QUE SE BLITEE EN RELACION
        # A LA PANTALLA, NO AL FORM DE INICIO

        form_ranking = FormRanking(self._master,
                                   x=250,
                                   y=25,
                                   w=500,
                                   h=550,
                                   color_background=(220,0,220),
                                   color_border="White",
                                   border_size=5,
                                   active=True,
                                   path_img="Recursos/Window.png",
                                   scores=dic_score,
                                   margen_x=10,
                                   margen_y=100,
                                   espacio=10)
        

        self.show_dialog(form_ranking)


    def update_volumen(self, lista_eventos):

        self.volumen = self.slider_volumen.value
        self.label_volumen.set_text(f"{round(self.volumen*100)}%")
        pygame.mixer.music.set_volume(self.volumen)

    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):

        if self.verificar_dialog_result():

            if self.active:
                self.draw()
                self.render()

                for widget in self.lista_widgets:
                    widget.update(lista_eventos)

                self.update_volumen(lista_eventos)
        
        else:
            self.hijo.update(lista_eventos)

        return super().update(lista_eventos)
