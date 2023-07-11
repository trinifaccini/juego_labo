import pygame
from API_FORMS.GUI_button import Button

from API_FORMS.GUI_form import Form
from API_FORMS.GUI_form_estado_juego import CELESTE
from API_FORMS.GUI_label import Label
from API_FORMS.GUI_button_image import Button_Image
from API_FORMS.GUI_picture_box import PictureBox
from datos_juego import W

class FormReglas(Form):

    def __init__(self, screen,x,y,w,h, color_background, color_border, border_size,
                 active, path_img):

        super().__init__(screen, x,y, w,h,color_background, color_border, border_size, active)

        # CABECERAS

        self.label = Label(screen=self._slave,
                           x=0,
                           y=0,
                           w=w,
                           h=50,
                           text="REGLAS E INFORMACION",
                           font= "Recursos/Fonts/Snowes.ttf",
                           font_size=35,
                           font_color="White",
                           path_image="Recursos/bar.png")

        self.icono_vidas_jugador = PictureBox(self._slave, 20, 70, 50, 50,
                                  "Recursos/Interfaces/cabeza_esquiador.png")
        
        self.label_vidas = Label(screen=self._slave,
                           x=100,
                           y=70,
                           w=220,
                           h=50,
                           text="REPRESENTA LA VIDAS DEL JUGADOR",
                           font= "Recursos/Fonts/Snowes.ttf",
                           font_size=25,
                           font_color="White")

        self.icono_cantidad_enemigos = PictureBox(self._slave, 20, 140, 50, 50,
                                  "Recursos/Obstaculos/piedra.png")

        self.label_cantidad_enemigos = Label(screen=self._slave,
                           x=100,
                           y=140,
                           w=340,
                           h=50,
                           text="CANTIDAD DE ENEMIGOS A MATAR PARA PASAR DE NIVEL",
                           font= "Recursos/Fonts/Snowes.ttf",
                           font_size=25,
                           font_color="White")
        

        self.icono_vidas_boss = PictureBox(self._slave, 20, 210, 50, 50,
                                  "Recursos/Obstaculos/piedra.png")

        self.label_vidas_boss = Label(screen=self._slave,
                           x=100,
                           y=210,
                           w=380,
                           h=50,
                           text="REPRESENTA LA VIDA DEL BOSS - APARECERA EN EL TERCER NIVEL",
                           font= "Recursos/Fonts/Snowes.ttf",
                           font_size=25,
                           font_color="White")
        

        self.icono_flechas = PictureBox(self._slave, 0, 280, 90, 50,
                                  "Recursos/Interfaces/flechas.png")
        
        self.label_flechas = Label(screen=self._slave,
                           x=100,
                           y=280,
                           w=175,
                           h=50,
                           text="MOVIMIENTOS DEL JUGADOR",
                           font= "Recursos/Fonts/Snowes.ttf",
                           font_size=25,
                           font_color="White")

        self.icono_espacio = PictureBox(self._slave, 0, 350, 90, 50,
                                  "Recursos/Interfaces/space.png")

        self.label_espacio = Label(screen=self._slave,
                           x=100,
                           y=350,
                           w=125,
                           h=50,
                           text="DISPARO JUGADOR",
                           font= "Recursos/Fonts/Snowes.ttf",
                           font_size=25,
                           font_color="White")


        self.icono_hamburguesa = PictureBox(self._slave, w/2, 70, 50, 40,
                                  "Recursos/Obstaculos/hamburguesa.png")

        self.label_hamburguesa = Label(screen=self._slave,
                           x=w/2+80,
                           y=70,
                           w=145,
                           h=50,
                           text="+10 PUNTOS AL RECOGER",
                           font= "Recursos/Fonts/Snowes.ttf",
                           font_size=25,
                           font_color="White")
        
        self.icono_coca = PictureBox(self._slave, w/2+10, 140, 30, 50,
                                  "Recursos/Obstaculos/coca_dibujo.png")

        self.label_coca = Label(screen=self._slave,
                           x=w/2+80,
                           y=140,
                           w=145,
                           h=50,
                           text="+100 VIDAS AL RECOGER",
                           font= "Recursos/Fonts/Snowes.ttf",
                           font_size=25,
                           font_color="White")
        
        self.icono_arbol = PictureBox(self._slave, w/2+10, 210, 40, 110,
                                  "Recursos/Obstaculos/arbol_1.png")
        
        self.label_arbol = Label(screen=self._slave,
                           x=w/2+80,
                           y=240,
                           w=145,
                           h=50,
                           text="RESTA PUNTOS AL TOCAR",
                           font= "Recursos/Fonts/Snowes.ttf",
                           font_size=25,
                           font_color="White")
        
        self.icono_piedra = PictureBox(self._slave, w/2+10, 330, 50, 60,
                                  "Recursos/Obstaculos/snow_1b.png")
        
        self.label_piedra = Label(screen=self._slave,
                           x=w/2+80,
                           y=340,
                           w=145,
                           h=50,
                           text="RESTA PUNTOS AL TOCAR",
                           font= "Recursos/Fonts/Snowes.ttf",
                           font_size=25,
                           font_color="White")

        self.boton_atras = Button_Image(self._slave,
                                           x, y, w-50, h-50,
                                           50, 50,
                                           "Recursos/Interfaces/flecha.png",
                                           self.btn_back_click, "x")

        self.boton_historia = Button(self._slave, x, y, w-150, 70,
                                 150,40,CELESTE, "Blue", self.btn_historia_click,
                                 "Nombre", "HISTORIA >", "Recursos/Fonts/Snowes.ttf", 30, "Black")


        ######

        self.lista_widgets.append(self.label)
        self.lista_widgets.append(self.label_vidas)
        self.lista_widgets.append(self.boton_atras)
        self.lista_widgets.append(self.icono_vidas_jugador)
        self.lista_widgets.append(self.icono_cantidad_enemigos)
        self.lista_widgets.append(self.label_cantidad_enemigos)
        self.lista_widgets.append(self.icono_vidas_boss)
        self.lista_widgets.append(self.label_vidas_boss)
        self.lista_widgets.append(self.icono_flechas)
        self.lista_widgets.append(self.label_flechas)
        self.lista_widgets.append(self.icono_espacio)
        self.lista_widgets.append(self.label_espacio)
        self.lista_widgets.append(self.icono_hamburguesa)
        self.lista_widgets.append(self.label_hamburguesa)
        self.lista_widgets.append(self.icono_coca)
        self.lista_widgets.append(self.label_coca)
        self.lista_widgets.append(self.icono_piedra)
        self.lista_widgets.append(self.icono_arbol)
        self.lista_widgets.append(self.label_piedra)
        self.lista_widgets.append(self.label_arbol)
        self.lista_widgets.append(self.boton_historia)


    def btn_historia_click(self, param) -> None:
        print("apreto")

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
