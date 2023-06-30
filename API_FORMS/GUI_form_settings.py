import pygame
from pygame.locals import * 

from API_FORMS.GUI_form import Form
from API_FORMS.GUI_button import Button
from API_FORMS.GUI_form_niveles import FormNiveles
from API_FORMS.GUI_textbox import TextBox
from API_FORMS.GUI_label import Label
from API_FORMS.GUI_slider import Slider
from API_FORMS.GUI_button_image import Button_Image
from API_FORMS.GUI_form_ranking import FormRanking
from config_db import buscar_usuario_db, insertar_jugador, traer_ranking_db

CELESTE = (64, 207, 255)

class FormInicio(Form):

    def __init__(self, screen,x,y,w,h, path_image, color_background = None, color_border="Magenta", border_size=-1,
                 active=True):

        super().__init__(screen, x,y, w,h,color_background, color_border, border_size, active)

        self.volumen = 0.2
        self.flag_play = True
        self.usuario_existente = False
        self.flag_jugar = False
        self.nivel = 0

        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image

        pygame.mixer.init()

        ######

        ancho_label = 250
        alto_label = 40
        ancho_txt = 200
        alto_txt = 35

        pos_x = w/2 - 250
        pos_x_label_uno = w/4 - ancho_label/2
        pos_x_label_dos = (w/4)*3 - ancho_label/2

        pos_x_txt_uno = w/4 - ancho_txt/2
        pos_x_txt_dos = (w/4)*3 - ancho_txt/2

        y_uno = 90
        espacio = 15

        ancho_btn_ranking = 50


        self.label_bienvenida = Label(self._slave, pos_x, 10, 500, 50,
                                   "BIENVENIDO", "Recursos/Fonts/Snowes.ttf", 40, "White",
                                   "Recursos/Interfaces/interfaces_2.png")

        self.usuario_jugador = ""

        self.label_jugador_nuevo = Label(self._slave,
                                         pos_x_label_uno, y_uno,ancho_label, alto_label,
                                         "NUEVO JUGADOR", "Recursos/Fonts/Snowes.ttf", 25,
                                         "White", "Recursos/Interfaces/interfaces.png")

        self.nombre_jugador = TextBox(self._slave, x,y,
                                      pos_x_txt_uno, y_uno + alto_label + espacio,
                                      ancho_txt,alto_txt,
                                      "Grey", "White", CELESTE, CELESTE, 5,
                                      "Recursos/Fonts/Snowes.ttf", 20, "Black")

        self.apellido_jugador = TextBox(self._slave, x,y,
                                        pos_x_txt_uno, y_uno + alto_label + alto_txt + espacio*2,
                                        ancho_txt,alto_txt,
                                        "Grey", "White", CELESTE, CELESTE, 5,
                                        "Recursos/Fonts/Snowes.ttf", 20, "Black")

        self.usuario_jugador_nuevo = TextBox(self._slave, x,y,
                                       pos_x_txt_uno, y_uno + alto_label + alto_txt*2 + espacio*3,
                                       ancho_txt, alto_txt,
                                       "Grey", "White", CELESTE, CELESTE, 5,
                                       "Recursos/Fonts/Snowes.ttf", 20, "Black")

        self.boton_crear_jugar = Button(self._slave, x, y,
                                 pos_x_txt_uno, y_uno + alto_label+ alto_txt*3 + espacio*4,
                                 ancho_txt, 50,
                                 CELESTE, "Blue", self.btn_crear_jugar_click,
                                 "Nombre", "JUGAR", "Recursos/Fonts/Snowes.ttf", 20, "Black")
        
        self.label_jugador_existente = Label(self._slave, pos_x_label_dos, y_uno,
                                             ancho_label, alto_label,
                                             "JUGADOR EXISTENTE", "Recursos/Fonts/Snowes.ttf", 25, 
                                             "White", "Recursos/Interfaces/interfaces.png")

        self.usuario_jugador_existente = TextBox(self._slave, x,y,
                                       pos_x_txt_dos, y_uno + alto_label + espacio,
                                       ancho_txt, alto_txt,
                                       "Grey", "White", CELESTE, CELESTE, 5,
                                       "Recursos/Fonts/Snowes.ttf", 20, "Black")

        self.boton_jugar = Button(self._slave, x, y,
                                 pos_x_txt_dos,  y_uno + alto_txt + alto_label + espacio*2, ancho_txt, 50,
                                 CELESTE, "Blue", self.btn_jugar_click,
                                 "Nombre", "JUGAR", "Recursos/Fonts/Snowes.ttf", 20, "Black")
        

        self.boton_play = Button(self._slave, x, y,
                                 300, 50, 100, 50,
                                 "Red", "Blue", self.btn_play_click,
                                 "Nombre", "PAUSE", "Recursos/Fonts/Snowes.ttf", 20, "Black")


        self.label_volumen = Label(self._slave, 700, 100, 100, 30,
                                   "20%", "Recursos/Fonts/Snowes.ttf", 12, "White", "Recursos/Table.png")

        self.slider_volumen = Slider(self._slave, x,y, 300, 200, 500, 15,
                                     self.volumen, "Blue", "White")

        self.boton_ranking = Button_Image(self._slave, x, y,
                                 w/2 - ancho_btn_ranking/2, 200,
                                 ancho_btn_ranking, ancho_btn_ranking,
                                 "Recursos/Menu_BTN.png",
                                 self.btn_ranking_click, "x")


        ######

        self.lista_widgets.append(self.label_bienvenida)
        self.lista_widgets.append(self.label_jugador_nuevo)
        self.lista_widgets.append(self.label_jugador_existente)
        self.lista_widgets.append(self.nombre_jugador)
        self.lista_widgets.append(self.apellido_jugador)
        self.lista_widgets.append(self.usuario_jugador_nuevo)
        self.lista_widgets.append(self.usuario_jugador_existente)
        # self.lista_widgets.append(self.boton_play)
        self.lista_widgets.append(self.boton_crear_jugar)
        self.lista_widgets.append(self.boton_jugar)
        #self.lista_widgets.append(self.label_volumen)
        #self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.boton_ranking)

        pygame.mixer.music.load("Recursos/Audio/musica.mp3")
        pygame.mixer.music.set_volume(self.volumen)
        #pygame.mixer.music.play(-1) # bucle

        self.render()

    def btn_play_click(self, param):


        if self.flag_play:
            pygame.mixer.music.pause()
            self.boton_play._color_background = "Cyan"
            self.boton_play.set_text("PLAY")

        else:
            pygame.mixer.music.unpause()
            self.boton_play._color_background = "Red"
            self.boton_play.set_text("PAUSE")

        self.flag_play = not self.flag_play

    def btn_crear_jugar_click(self, param):

        if(self.nombre_jugador.get_text() != "" and self.usuario_jugador_nuevo.get_text() != ""
           and self.apellido_jugador.get_text() != ""):

            guardado = insertar_jugador(self.nombre_jugador.get_text(),
                                        self.apellido_jugador.get_text(),0, 0,
                                        self.usuario_jugador_nuevo.get_text(), "jugadores.db")

            if guardado:
                self.usuario_jugador = {
                    "usuario": self.usuario_jugador_nuevo.get_text(),
                    "puntos": 0,
                    "nivel_max": 0
                }

                self.flag_jugar = True

        else:
            print("falta completar datos")

    def btn_jugar_click(self, param):

        if(self.usuario_jugador_existente.get_text() != ""):

            usuario = buscar_usuario_db("jugadores.db", self.usuario_jugador_existente.get_text())

            if usuario:
                self.usuario_jugador = {
                    "usuario": usuario[0],
                    "puntos": usuario[1],
                    "nivel_max": usuario[2]
                }

                form_niveles = FormNiveles(self._master,
                                   x=self._w/2-(500/2),
                                   y=25,
                                   w=500,
                                   h=550,
                                   path_image="Recursos/Window.png",
                                   nivel_max=self.usuario_jugador['nivel_max'],
                                   color_background=(220,0,220),
                                   color_border="White",
                                   border_size=-1,
                                   active=True)

                self.show_dialog(form_niveles)

            else:
                print("no existeee")

        else:
            print("falta completar datos")


    def btn_ranking_click(self, param):

        #print(self.nombre_jugador.get_text())

        dic_score = traer_ranking_db("jugadores.db")

        # LE PASAMOS EL MASTER PORQUE ESTE FORM QUEREMOS QUE SE BLITEE EN RELACION
        # A LA PANTALLA, NO AL FORM DE INICIO

        form_ranking = FormRanking(self._master,
                                   x=self._w/2-(500/2),
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
        self.draw()

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
