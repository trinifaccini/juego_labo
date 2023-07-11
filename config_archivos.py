'''
sdfsdf
'''

import datetime

def escribir_excepcion(nombre_archivo:str, excepcion) -> None:

    try:
        hora_actual = datetime.datetime.now()

        archivo = open(nombre_archivo, "a", encoding="utf-8")
        archivo.write(f"{hora_actual}: {excepcion}\n")
        archivo.close()
    except Exception as e:
        print("Excepcion:", e)
