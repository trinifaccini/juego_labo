import pygame
from API_FORMS.GUI_button import Button

from API_FORMS.GUI_form import Form
from API_FORMS.GUI_form_estado_juego import CELESTE
from API_FORMS.GUI_label import Label
from API_FORMS.GUI_button_image import Button_Image
from API_FORMS.GUI_picture_box import PictureBox

class FormNivel(Form):

    def __init__(self, screen,x,y,w,h, color_background, color_border, border_size,
                 active, nivel:dict):

        super().__init__(screen, x,y, w,h,color_background, color_border, border_size, active)
        self.jugando = True
        self.pausado = True

        # CABECERAS

        self.label = Label(screen=self._slave,
                           x=0,
                           y=0,
                           w=w,
                           h=50,
                           text=f"PROXIMO NIVEL: {nivel['numero']}",
                           font= "Recursos/Fonts/Snowes.ttf",
                           font_size=35,
                           font_color="White",
                           path_image="Recursos/bar.png")

        self.label_enemigos = Label(screen=self._slave,
                           x=100,
                           y=70,
                           w=300,
                           h=50,
                           text=f"DEBERAS MATAR AL ENEMIGO DE TIPO: {nivel['tipo_enemigo']}",
                           font= "Recursos/Fonts/Snowes.ttf",
                           font_size=30,
                           font_color="White")

        self.label_cantidad = Label(screen=self._slave,
                           x=110,
                           y=130,
                           w=300,
                           h=50,
                           text=f"CANTIDAD A MATAR PARA PASAR DE NIVEL: {nivel['cantidad']}",
                           font= "Recursos/Fonts/Snowes.ttf",
                           font_size=30,
                           font_color="White")

        self.icono_enemigo = PictureBox(self._slave, 0, 70, 100,100,nivel['img_enemigo'])

        self.label_descripcion_uno = Label(screen=self._slave,
                           x=0,
                           y=170,
                           w=w,
                           h=150,
                           text="TENDRAS 60 SEGUNDOS PARA ALCANZAR EL OBJETIVO. DE LO CONTRARIO PERDERAS",
                           font= "Recursos/Fonts/Snowes.ttf",
                           font_size=30,
                           font_color="White")
        
        self.label_descripcion_dos = Label(screen=self._slave,
                           x=0,
                           y=170,
                           w=w,
                           h=150,
                           text="NO OLVIDES DE TOMAR LA MAYOR CANTIDAD DE COCA-COLAS QUE PUEDAS, LAS VAS A NECESITAR..",
                           font= "Recursos/Fonts/Snowes.ttf",
                           font_size=30,
                           font_color="White")

        self.boton_continuar = Button(self._slave, x, y, w-200, h-50,
                                 200,40,CELESTE, "Blue", self.btn_continuar_click,
                                 "Nombre", "COMENZAR NIVEL", 
                                 "Recursos/Fonts/Snowes.ttf",30, "Black")

        self.boton_home = Button_Image(self._slave,
                                         x, y, 0, h-50,50, 50,
                                         "Recursos/Interfaces/home.png",
                                          self.btn_home_click, "x")
        ######

        self.lista_widgets.append(self.label)
        self.lista_widgets.append(self.label_enemigos)
        self.lista_widgets.append(self.label_cantidad)
        self.lista_widgets.append(self.icono_enemigo)
        self.lista_widgets.append(self.label_descripcion_uno)
        self.lista_widgets.append(self.label_descripcion_dos)
        self.lista_widgets.append(self.boton_continuar)
        self.lista_widgets.append(self.boton_home)


    def btn_continuar_click(self, param) -> None:
        self.pausado = False
        self.end_dialog()

    def btn_home_click(self, param) -> None:

        pygame.mixer.init()

        self.jugando = False
        self.pausado = False
        pygame.mixer.music.load("Recursos/Audio/fondo.mp3")
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume())
        pygame.mixer.music.play(-1) # bucle
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
