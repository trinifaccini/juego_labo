'''
CLASE PERSONAJE
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=arguments-differ

from clase_objeto_animado import ObjetoAnimado
from clase_proyectil import Proyectil

class Personaje(ObjetoAnimado):

    def __init__(self, tamanio: tuple, pos_inicial: tuple, animaciones, velocidad: int,
                 potencia_salto: int, vidas:int, img_proyectil:str, danio:int):

        super().__init__(tamanio, pos_inicial, animaciones, velocidad, potencia_salto)

        self.vidas = vidas
        self.img_proyectil = img_proyectil
        self.lista_proyectiles = []
        self.danio = danio

    def lanzar_proyectil(self, velocidad):

        if self.accion == "izquierda":
            velocidad = velocidad * -1

        proyectil = Proyectil(
            (20, 20),(self.lados['main'].centerx, self.lados['left'].y),
            -500, 0, velocidad, self.img_proyectil)

        self.lista_proyectiles.append(proyectil)

    def update_proyectiles(self, pantalla):
        for proyectil in self.lista_proyectiles:
            proyectil.update(pantalla)

    # VERIFICO COLISION DE PROYECTIL CON CUALQUIER PERSONAJE (SEA ENEMIGO O JUGADOR)
    # SI COLISIONA LO BORRO DE LA LISTA
    def verificar_colision_proyectil(self, personajes):

        for personaje in personajes:
            for proyectil in personaje.lista_proyectiles:
                if self.lados['main'].colliderect(proyectil.lados['main']):
                    print("COLISIONO PROYECTIL")
                    self.vidas += proyectil.cambio_vida
                    lista_aux = personaje.lista_proyectiles
                    lista_aux.remove(proyectil)
                    del proyectil

    def definir_accion(self):

        self.accion = "quieto"

    def update(self, pantalla, lista_plataformas, personajes):

        # Actualizo los proyectiles acá porque ambos tipos de personaje tienen
        # proyectiles
        self.update_proyectiles(pantalla)

        self.verificar_colision_proyectil(personajes)

        super().update(pantalla, lista_plataformas)
