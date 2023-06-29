import pygame
from pygame.locals import * 

from API_FORMS.GUI_form import Form
from API_FORMS.GUI_label import Label
from API_FORMS.GUI_button_image import Button_Image

class FormRanking(Form):

    def __init__(self, screen,x,y,w,h,color_background, color_border, border_size, active,
                 path_img, scores, margen_x, margen_y, espacio):

        super().__init__(screen, x,y, w,h,color_background, color_border, border_size, active)

        aux_imagen = pygame.image.load(path_img)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))

        self._slave = aux_imagen
        self._scores = scores
        self._margen_x = margen_x
        self._margen_y = margen_y

        pos_x_label = margen_x + 10
        ancho_label = w/2-margen_x-10

        ######

        # CABECERAS

        self.label_usuario = Label(self._slave, pos_x_label, 30,
                                   ancho_label, 50, "USUARIO", "Recursos/Fonts/Snowes.ttf", 30,
                                   "White", "Recursos/bar.png")

        self.label_puntos = Label(self._slave, pos_x_label + ancho_label, 30,
                                  w/2-margen_x-10, 50, "PUNTOS", "Recursos/Fonts/Snowes.ttf", 30,
                                  "White", "Recursos/bar.png")


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
                                        font_size= 30,
                                        font_color= (0,255,0),
                                        path_image="Recursos/home.png"
                                        )

        ######

        self.lista_widgets.append(self.label_usuario)
        self.lista_widgets.append(self.label_puntos)
        self.lista_widgets.append(self.boton_home)

        pos_inicial_y = margen_y

        for jugador in self._scores:
            pos_inicial_x = margen_x
            for x in jugador:
                cadena = ""
                cadena += f"{x}"
                aux = Label(self._slave, pos_inicial_x, pos_inicial_y,
                            w/2-margen_x, 50, cadena, "Recursos/Fonts/Snowes.ttf", 25,
                            "White", "Recursos/Table.png")
                self.lista_widgets.append(aux)
                pos_inicial_x += w/2 - margen_x

            pos_inicial_y += 50 + espacio


        # self.render()

    def btn_home_click(self, param) -> None:

        self.end_dialog()


    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):

        if self.active:

            for widget in self.lista_widgets:
                widget.update(lista_eventos)

            self.draw()
            # self.render()

        return super().update(lista_eventos)
