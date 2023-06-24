# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

'''
ARCHIVO CLASE NIVEL
'''

class Nivel():

    def __init__(self, fondo, plataformas, enemigos, items, tiempo, puntos_requeridos, ) -> None:

        self.fondo = fondo
        self.tiempo = tiempo
        self.enemigos = enemigos
        self.items = items
        self.plataformas = plataformas # las plataformas van a venir con las trampas
        self.puntos_requeridos = puntos_requeridos

    def posicionar_jugador(self) -> None:
        pass

    def posicionar_plataformas(self, rect_pantalla) -> None:

        for plataforma in self.plataformas:
            plataforma.update(rect_pantalla)

    def posicionar_enemigos(self, rect_pantalla, jugador) -> None:

        for enemigo in self.enemigos:

            enemigo.update(rect_pantalla, self.plataformas, jugador)
            lista_aux = enemigo.lista_proyectiles
            for x in enemigo.lista_proyectiles:
                x.update(rect_pantalla)
                if x.colisiono:
                    lista_aux.remove(x)
                    del x


    def posicionar_items(self, rect_pantalla) -> None:

        items_aux = self.items

        for item in self.items:
            item.update(rect_pantalla)
            if item.colisiono:
                items_aux.remove(item)
                del item

    def update(self, rect_pantalla, jugador, keys) -> None:

        rect_pantalla.blit(self.fondo, (0, 0))

        self.posicionar_plataformas(rect_pantalla)
        self.posicionar_enemigos(rect_pantalla, jugador)
        self.posicionar_items(rect_pantalla)

        jugador.update(rect_pantalla, self.plataformas, self.items, self.enemigos, keys)

    def update_personalizado(self, jugador, keys):

        jugador.update_personalizado(self.enemigos, keys)
