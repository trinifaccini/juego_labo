"""
CONFIGURACIONES DE IMAGEN
"""

# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=consider-using-enumerate
# pylint: disable=pointless-string-statement

import pygame

#########################


def girar_imagenes(lista, flip_x, flip_y) -> list:
    lista_girada = []

    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada


def reescalar_imagen(lista_imagenes, alto, ancho):

    for i in range(len(lista_imagenes)):  # en un rango, si modifica
        lista_imagenes[i] = pygame.transform.scale(
            lista_imagenes[i], (alto, ancho))


def obtener_rectangulos(principal: pygame.Rect) -> dict:
    diccionario = {}

    diccionario = {
        "main": principal,
        "bottom": pygame.Rect(principal.left, principal.bottom-10, principal.width, 10),
        "right": pygame.Rect(principal.right-5, principal.top, 5, principal.height),
        "left": pygame.Rect(principal.left, principal.top, 5, principal.height),
        "top": pygame.Rect(principal.left, principal.top, principal.width, 10)
    }

    return diccionario


def dibujar_borde_rectangulos(pantalla, lados_rectangulo: dict, color: str):

    for lado in lados_rectangulo:
        pygame.draw.rect(pantalla, color, lados_rectangulo[lado], 2)


def deepcopy_dict_animaciones(animaciones:dict) -> dict:

    animaciones_aux = {}
    for animacion in animaciones:
        lista_aux = []
        for i in animaciones[animacion]:
            i_aux = pygame.Surface.copy(i)
            lista_aux.append(i_aux)
        animaciones_aux.update({animacion : lista_aux})

    return animaciones_aux


###################


# Definimos los fotogramas de cada animacion

personaje_quieto_derecha = [
    pygame.image.load("Recursos/Personajes/Normal/Esquiador/Quieto/esquiador_quieto_0.png"),
    pygame.image.load("Recursos/Personajes/Normal/Esquiador/Quieto/esquiador_quieto_1.png"),
    pygame.image.load("Recursos/Personajes/Normal/Esquiador/Quieto/esquiador_quieto_2.png"),
    pygame.image.load("Recursos/Personajes/Normal/Esquiador/Quieto/esquiador_quieto_3.png")
    ]

personaje_quieto_izquierda = girar_imagenes(personaje_quieto_derecha, True, False)

personaje_camina_derecha = [
    pygame.image.load("Recursos/Personajes/Normal/Esquiador/Moviendose/esquiador_moviendose_0.png"),
    pygame.image.load("Recursos/Personajes/Normal/Esquiador/Moviendose/esquiador_moviendose_1.png"),
    pygame.image.load("Recursos/Personajes/Normal/Esquiador/Moviendose/esquiador_moviendose_2.png"),
    pygame.image.load("Recursos/Personajes/Normal/Esquiador/Moviendose/esquiador_moviendose_3.png")
]

personaje_camina_izquierda = girar_imagenes(personaje_camina_derecha, True, False)

personaje_salta_derecha = [
    pygame.image.load("Recursos/Personajes/Normal/Esquiador/Saltando/esquiador_saltando_0.png"),
]

personaje_salta_izquierda = girar_imagenes(personaje_salta_derecha, True, False)


personaje_atacado_derecha = [
    pygame.image.load("Recursos/Personajes/Normal/Esquiador/Atacado/atacado.png"),
]

personaje_atacado_izquierda = girar_imagenes(personaje_atacado_derecha, True, False)

personaje_escondido_derecha = [
    pygame.image.load("Recursos/Personajes/Normal/Esquiador/Escondido/escondido.png"),
]

personaje_escondido_izquierda = girar_imagenes(personaje_escondido_derecha, True, False)



###########################################################################

oso_quieto_derecha = [
    pygame.image.load("Recursos/Personajes/Normal/Oso/Quieto/oso_quieto_0.png"),
    ]

oso_quieto_izquierda = girar_imagenes(oso_quieto_derecha, True, False)

oso_salta_derecha = [
    pygame.image.load("Recursos/Personajes/Normal/Oso/Quieto/oso_quieto_0.png"),
    ]

oso_salta_izquierda = girar_imagenes(oso_salta_derecha, True, False)

oso_camina_derecha = [
    pygame.image.load("Recursos/Personajes/Normal/Oso/Camina/oso_camina_0.png"),
    pygame.image.load("Recursos/Personajes/Normal/Oso/Camina/oso_camina_1.png"),
    pygame.image.load("Recursos/Personajes/Normal/Oso/Camina/oso_camina_2.png"),
    pygame.image.load("Recursos/Personajes/Normal/Oso/Camina/oso_camina_3.png"),
    pygame.image.load("Recursos/Personajes/Normal/Oso/Camina/oso_camina_4.png"),
    pygame.image.load("Recursos/Personajes/Normal/Oso/Camina/oso_camina_5.png"),
    pygame.image.load("Recursos/Personajes/Normal/Oso/Camina/oso_camina_6.png"),
    pygame.image.load("Recursos/Personajes/Normal/Oso/Camina/oso_camina_7.png"),

]

oso_camina_izquierda = girar_imagenes(oso_camina_derecha, True, False)

###########################################################################

monstruo_quieto_derecha = [
    pygame.image.load("Recursos/Personajes/Normal/Monstruo/Quieto/tile000.png"),
    pygame.image.load("Recursos/Personajes/Normal/Monstruo/Quieto/tile001.png"),
    pygame.image.load("Recursos/Personajes/Normal/Monstruo/Quieto/tile002.png"),
    pygame.image.load("Recursos/Personajes/Normal/Monstruo/Quieto/tile003.png")
    ]

monstruo_quieto_izquierda = girar_imagenes(monstruo_quieto_derecha, True, False)

monstruo_camina_izquierda = [
    pygame.image.load("Recursos/Personajes/Normal/Monstruo/Camina/tile006.png"),
    pygame.image.load("Recursos/Personajes/Normal/Monstruo/Camina/tile007.png"),
    pygame.image.load("Recursos/Personajes/Normal/Monstruo/Camina/tile008.png"),
    pygame.image.load("Recursos/Personajes/Normal/Monstruo/Camina/tile009.png"),
    pygame.image.load("Recursos/Personajes/Normal/Monstruo/Camina/tile010.png"),

]

monstruo_camina_derecha= girar_imagenes(monstruo_camina_izquierda, True, False)

monstruo_ataca_izquierda = [
    pygame.image.load("Recursos/Personajes/Normal/Monstruo/Ataca/tile011.png"),
    pygame.image.load("Recursos/Personajes/Normal/Monstruo/Ataca/tile012.png"),
    pygame.image.load("Recursos/Personajes/Normal/Monstruo/Ataca/tile013.png"),
    pygame.image.load("Recursos/Personajes/Normal/Monstruo/Ataca/tile014.png"),
    pygame.image.load("Recursos/Personajes/Normal/Monstruo/Ataca/tile015.png"),
    ]

monstruo_ataca_derecha = girar_imagenes(monstruo_ataca_izquierda, True, False)

monstruo_salta_izquierda = [
    pygame.image.load("Recursos/Personajes/Normal/Monstruo/Quieto/tile000.png"),
]

monstruo_salta_derecha = girar_imagenes(monstruo_salta_izquierda, True, False)


###############

yeti_quieto_derecha = [
    pygame.image.load("Recursos/Personajes/Normal/Yeti/Quieto/yeti_quieto_0.png"),
    ]

yeti_quieto_izquierda = girar_imagenes(yeti_quieto_derecha, True, False)

yeti_camina_derecha = [
    pygame.image.load("Recursos/Personajes/Normal/Yeti/Camina/yeti_camina_0.png"),
    pygame.image.load("Recursos/Personajes/Normal/Yeti/Camina/yeti_camina_1.png"),
    pygame.image.load("Recursos/Personajes/Normal/Yeti/Camina/yeti_camina_2.png"),
    pygame.image.load("Recursos/Personajes/Normal/Yeti/Camina/yeti_camina_3.png"),
    pygame.image.load("Recursos/Personajes/Normal/Yeti/Camina/yeti_camina_4.png"),

]

yeti_camina_izquierda = girar_imagenes(yeti_camina_derecha, True, False)

yeti_ataca_derecha = [
    pygame.image.load("Recursos/Personajes/Normal/Yeti/Ataca/yeti_ataca_0.png"),
    pygame.image.load("Recursos/Personajes/Normal/Yeti/Ataca/yeti_ataca_1.png"),
    pygame.image.load("Recursos/Personajes/Normal/Yeti/Ataca/yeti_ataca_2.png"),
    pygame.image.load("Recursos/Personajes/Normal/Yeti/Ataca/yeti_ataca_3.png"),
    pygame.image.load("Recursos/Personajes/Normal/Yeti/Ataca/yeti_ataca_4.png"),
    pygame.image.load("Recursos/Personajes/Normal/Yeti/Ataca/yeti_ataca_5.png"),
    ]

yeti_ataca_izquierda = girar_imagenes(yeti_ataca_derecha, True, False)

yeti_ataca_especial_derecha = [
    pygame.image.load("Recursos/Personajes/Normal/Yeti/Ataca/yeti_ataca_0.png"),
    ]

yeti_ataca_especial_izquierda = girar_imagenes(yeti_ataca_especial_derecha, True, False)

yeti_salta_derecha = [
    pygame.image.load("Recursos/Personajes/Normal/Yeti/Quieto/yeti_quieto_0.png"),
]

yeti_salta_izquierda = girar_imagenes(yeti_salta_derecha, True, False)


###########################################################################

diccionario_animaciones_personaje_normal = {}
diccionario_animaciones_personaje_normal = {
    "quieto_derecha": personaje_quieto_derecha,
    "quieto_izquierda": personaje_quieto_izquierda,
    "camina_derecha": personaje_camina_derecha,
    "camina_izquierda": personaje_camina_izquierda,
    "salta_derecha": personaje_salta_derecha,
    "salta_izquierda": personaje_salta_izquierda,
    "atacado_derecha": personaje_atacado_derecha,
    "atacado_izquierda": personaje_atacado_izquierda,
    "escondido_derecha": personaje_escondido_derecha,
    "escondido_izquierda": personaje_escondido_izquierda
}


diccionario_animaciones_oso_normal = {}
diccionario_animaciones_oso_normal = {
    "quieto_derecha": oso_quieto_derecha,
    "quieto_izquierda": oso_quieto_izquierda,
    "salta_derecha": oso_salta_derecha,
    "salta_izquierda": oso_quieto_izquierda,
    "camina_derecha": oso_camina_derecha,
    "camina_izquierda": oso_camina_izquierda
}

diccionario_animaciones_yeti_normal = {}

diccionario_animaciones_yeti_normal = {
    "quieto_derecha": yeti_quieto_derecha,
    "quieto_izquierda": yeti_quieto_izquierda,
    "salta_derecha": yeti_salta_derecha,
    "salta_izquierda": yeti_salta_izquierda,
    "camina_derecha": yeti_camina_derecha,
    "camina_izquierda": yeti_camina_izquierda,
    "ataca_derecha": yeti_ataca_derecha,
    "ataca_izquierda": yeti_ataca_izquierda,
    "ataca_especial_derecha": yeti_ataca_especial_derecha,
    "ataca_especial_izquierda": yeti_ataca_especial_izquierda
}


diccionario_animaciones_monstruo_normal = {
    "quieto_derecha": monstruo_quieto_derecha,
    "quieto_izquierda": monstruo_quieto_izquierda,
    "salta_derecha": monstruo_salta_derecha,
    "salta_izquierda": monstruo_salta_izquierda,
    "camina_derecha": monstruo_camina_derecha,
    "camina_izquierda": monstruo_camina_izquierda,
    "ataca_derecha": monstruo_ataca_derecha,
    "ataca_izquierda": monstruo_ataca_izquierda,
}

'''
sdf
sf
sdf
s
df
sdf
s
df
sdf

sdf
'''

personaje_quieto_derecha_rojo = [
    pygame.image.load("Recursos/Personajes/Rojo/Esquiador/Quieto/esquiador_quieto_0.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Esquiador/Quieto/esquiador_quieto_1.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Esquiador/Quieto/esquiador_quieto_2.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Esquiador/Quieto/esquiador_quieto_3.png")
    ]

personaje_quieto_izquierda_rojo = girar_imagenes(personaje_quieto_derecha_rojo, True, False)

personaje_camina_derecha_rojo = [
    pygame.image.load("Recursos/Personajes/Rojo/Esquiador/Moviendose/esquiador_moviendose_0.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Esquiador/Moviendose/esquiador_moviendose_1.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Esquiador/Moviendose/esquiador_moviendose_2.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Esquiador/Moviendose/esquiador_moviendose_3.png")
]

personaje_camina_izquierda_rojo = girar_imagenes(personaje_camina_derecha_rojo, True, False)

personaje_salta_derecha_rojo = [
    pygame.image.load("Recursos/Personajes/Rojo/Esquiador/Saltando/esquiador_saltando_0.png"),
]

personaje_salta_izquierda_rojo = girar_imagenes(personaje_salta_derecha_rojo, True, False)


personaje_atacado_derecha_rojo = [
    pygame.image.load("Recursos/Personajes/Rojo/Esquiador/Atacado/atacado.png"),
]

personaje_atacado_izquierda_rojo = girar_imagenes(personaje_atacado_derecha_rojo, True, False)

personaje_escondido_derecha_rojo = [
    pygame.image.load("Recursos/Personajes/Normal/Esquiador/Escondido/escondido.png"),
]

personaje_escondido_izquierda_rojo = girar_imagenes(personaje_escondido_derecha, True, False)




###########################################################################

oso_quieto_derecha_rojo = [
    pygame.image.load("Recursos/Personajes/Rojo/Oso/Quieto/oso_quieto_0.png"),
    ]

oso_quieto_izquierda_rojo = girar_imagenes(oso_quieto_derecha_rojo, True, False)

oso_salta_derecha_rojo = [
    pygame.image.load("Recursos/Personajes/Rojo/Oso/Quieto/oso_quieto_0.png"),
    ]

oso_salta_izquierda_rojo = girar_imagenes(oso_salta_derecha_rojo, True, False)

oso_camina_derecha_rojo = [
    pygame.image.load("Recursos/Personajes/Rojo/Oso/Camina/oso_camina_0.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Oso/Camina/oso_camina_1.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Oso/Camina/oso_camina_2.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Oso/Camina/oso_camina_3.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Oso/Camina/oso_camina_4.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Oso/Camina/oso_camina_5.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Oso/Camina/oso_camina_6.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Oso/Camina/oso_camina_7.png"),

]

oso_camina_izquierda_rojo = girar_imagenes(oso_camina_derecha_rojo, True, False)

###########################################################################

yeti_quieto_derecha_rojo = [
    pygame.image.load("Recursos/Personajes/Rojo/Yeti/Quieto/yeti_quieto_0.png"),
    ]

yeti_quieto_izquierda_rojo = girar_imagenes(yeti_quieto_derecha_rojo, True, False)

yeti_camina_derecha_rojo = [
    pygame.image.load("Recursos/Personajes/Rojo/Yeti/Camina/yeti_camina_0.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Yeti/Camina/yeti_camina_1.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Yeti/Camina/yeti_camina_2.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Yeti/Camina/yeti_camina_3.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Yeti/Camina/yeti_camina_4.png"),

]

yeti_camina_izquierda_rojo = girar_imagenes(yeti_camina_derecha_rojo, True, False)

yeti_ataca_derecha_rojo = [
    pygame.image.load("Recursos/Personajes/Rojo/Yeti/Ataca/yeti_ataca_0.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Yeti/Ataca/yeti_ataca_1.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Yeti/Ataca/yeti_ataca_2.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Yeti/Ataca/yeti_ataca_3.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Yeti/Ataca/yeti_ataca_4.png"),
    pygame.image.load("Recursos/Personajes/Rojo/Yeti/Ataca/yeti_ataca_5.png"),
    ]

yeti_ataca_izquierda_rojo = girar_imagenes(yeti_ataca_derecha_rojo, True, False)

yeti_ataca_especial_derecha_rojo = [
    pygame.image.load("Recursos/Personajes/Rojo/Yeti/Ataca/yeti_ataca_0.png"),
    ]

yeti_ataca_especial_izquierda_rojo = girar_imagenes(yeti_ataca_especial_derecha_rojo, True, False)

yeti_salta_derecha_rojo = [
    pygame.image.load("Recursos/Personajes/Rojo/Yeti/Quieto/yeti_quieto_0.png"),
]

yeti_salta_izquierda_rojo = girar_imagenes(yeti_salta_derecha_rojo, True, False)


###########################################################################

diccionario_animaciones_personaje_rojo = {}
diccionario_animaciones_personaje_rojo = {
    "quieto_derecha": personaje_quieto_derecha_rojo,
    "quieto_izquierda": personaje_quieto_izquierda_rojo,
    "camina_derecha": personaje_camina_derecha_rojo,
    "camina_izquierda": personaje_camina_izquierda_rojo,
    "salta_derecha": personaje_salta_derecha_rojo,
    "salta_izquierda": personaje_salta_izquierda_rojo,
    "atacado_derecha": personaje_atacado_derecha_rojo,
    "atacado_izquierda": personaje_atacado_izquierda_rojo,
    "escondido_derecha": personaje_escondido_derecha_rojo,
    "escondido_izquierda": personaje_escondido_izquierda_rojo
}


diccionario_animaciones_oso_rojo = {}
diccionario_animaciones_oso_rojo = {
    "quieto_derecha": oso_quieto_derecha_rojo,
    "quieto_izquierda": oso_quieto_izquierda_rojo,
    "salta_derecha": oso_salta_derecha_rojo,
    "salta_izquierda": oso_quieto_izquierda_rojo,
    "camina_derecha": oso_camina_derecha_rojo,
    "camina_izquierda": oso_camina_izquierda
}

diccionario_animaciones_yeti_rojo = {}
diccionario_animaciones_yeti_rojo = {
    "quieto_derecha": yeti_quieto_derecha_rojo,
    "quieto_izquierda": yeti_quieto_izquierda_rojo,
    "salta_derecha": yeti_salta_derecha_rojo,
    "salta_izquierda": yeti_salta_izquierda_rojo,
    "camina_derecha": yeti_camina_derecha_rojo,
    "camina_izquierda": yeti_camina_izquierda_rojo,
    "ataca_derecha": yeti_ataca_derecha_rojo,
    "ataca_izquierda": yeti_ataca_izquierda_rojo,
    "ataca_especial_derecha": yeti_ataca_especial_derecha_rojo,
    "ataca_especial_izquierda": yeti_ataca_especial_izquierda_rojo
}

diccionario_animaciones_monstruo_rojo = {
    "quieto_derecha": monstruo_quieto_derecha,
    "quieto_izquierda": monstruo_quieto_izquierda,
    "salta_derecha": monstruo_salta_derecha,
    "salta_izquierda": monstruo_salta_izquierda,
    "camina_derecha": monstruo_camina_derecha,
    "camina_izquierda": monstruo_camina_izquierda,
    "ataca_derecha": monstruo_ataca_derecha,
    "ataca_izquierda": monstruo_ataca_izquierda,
}
