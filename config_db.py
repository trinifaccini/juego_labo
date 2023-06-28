'''
jfdj

'''
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
# pylint: disable=broad-exception-caught
# pylint: disable=invalid-name

import sqlite3

def insertar_jugador(nombre, apellido, nivel, puntos, usuario, nombre_db) -> None:

    insert = '''
        insert into Jugadores (nombre,apellido,nivel_max,puntos, usuario)
        values (?,?,?,?,?)
    '''

    with sqlite3.connect(nombre_db) as conexion:
        try:
            conexion.execute(insert, (nombre, apellido, nivel, puntos, usuario))
            return True
        except Exception as e:
            print("error", e)

def actualizar_jugador(nivel,puntos, usuario, nombre_db) -> None:

    update = "update Jugadores set nivel_max = ?, puntos = ? where usuario = ?"

    with sqlite3.connect(nombre_db) as conexion:
        try:
            conexion.execute(update, (nivel, puntos, usuario))
        except Exception as e:
            print("error", e)

def buscar_usuario_db(nombre_db, usuario) -> list:

    select = "SELECT usuario from Jugadores WHERE usuario = ?"

    with sqlite3.connect(nombre_db) as conexion:
        try:
            conexion.row_factory = lambda cursor, row: row[0]
            c = conexion.cursor()
            usuario = c.execute(select, (usuario,)).fetchall()
            return usuario
        
        except Exception as e:
            print("error", e)



def traer_ranking_db(nombre_db) -> list:

    select = "SELECT usuario, puntos from Jugadores WHERE puntos != 0 ORDER BY puntos desc limit 5"

    with sqlite3.connect(nombre_db) as conexion:
        try:

            # conexion.row_factory = lambda cursor, row: row[0]
            # c = conexion.cursor()
            usuarios = conexion.execute(select).fetchall()
            return list(usuarios)

        except Exception as e:
            print("error", e)

# buscar_usuario_db("jugadores.db", "triniiiii")
traer_ranking_db("jugadores.db")
