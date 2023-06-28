import pygame
import sys
from pygame.locals import *
from API_FORMS.GUI_form_inicio import FormInicio

pygame.init()

W = 1200
H = 600
FPS = 60

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W,H))

form_inicio = FormInicio(PANTALLA, 200, 100, 900, 350, "Recursos/Fondos/bg-icebergs-2.png")

while True:

    RELOJ.tick(FPS)

    eventos = pygame.event.get()

    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    keys = pygame.key.get_pressed()

    PANTALLA.fill("Black")
    form_inicio.update(eventos)

    pygame.display.flip()
