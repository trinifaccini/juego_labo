'''
jjj
'''

import sqlite3

sentencia_create = '''
                    create table Jugadores
                        (
                            id integer primary key,
                            nombre text,
                            apellido text,
                            nivel_max integer,
                            puntos integer,
                            usuario text UNIQUE
                        )
                    '''

sentencia_columna_tabla = '''
                        alter table Jugadores
                        add usuario text
                         '''

insertar_jugador = '''
                    insert into Jugadores (nombre,apellido,nivel_max,puntos, usuario)
                    values ("Lourdes", "Faccini", 2, 30, "trinif28")
                    '''

insertar_jugador_dos = '''
                    insert into Jugadores (nombre,apellido,nivel_max,puntos, usuario)
                    values (?,?,?,?,?)
                    '''

# conexion.execute(insertar_jugador_dos, ("Juan", "Fernandez", 3, 50, "marup"))

select = "select nombre, apellido from Jugadores order by puntos desc"
# sentencia = select
# cursor = conexion.execute(sentencia)

#         for fila in cursor:
#           print(fila)

update = "update Jugadores set puntos = 500 where usuario = 'marup'"
update_dos = "update Jugadores set puntos = 700 where usuario = ?"
usuario = "marup"
#conexion.execute(update_dos, (usuario,))

update_tres = "update Jugadores set puntos = ? where usuario = ?"
puntos = 300
#conexion.execute(update_dos, (puntos,usuario))

delete = "delete from Jugadores where usuario = ?"


with sqlite3.connect("jugadores.db") as conexion:
    try:
        conexion.execute(sentencia_create)
    except Exception as e:
        print("error")

