
from config_img import * 

def funciones_enemigo(enemigo, pantalla, lista_plataformas, jugador):
    enemigo.update(pantalla, lista_plataformas)
    dibujar_borde_rectangulos(pantalla, enemigo.lados, "Yellow")
    lista_aux = enemigo.lista_proyectiles
    for x in enemigo.lista_proyectiles:
        x.update(pantalla, jugador)
        dibujar_borde_rectangulos(pantalla, x.lados, "Magenta")
        if x.colisiono:
            print("PUNTOS", jugador.puntos)
            print("VIDA", jugador.vidas)
            lista_aux.remove(x)

def funciones_items(items, pantalla, jugador):

    items_aux = items
    for i in items:
        i.update(pantalla, jugador)
        dibujar_borde_rectangulos(pantalla, i.lados, "Blue")
        if i.colisiono:
            print("PUNTOS", jugador.puntos)
            print("VIDA", jugador.vidas)
            items_aux.remove(i)