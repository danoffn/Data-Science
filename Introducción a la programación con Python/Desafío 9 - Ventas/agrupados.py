from itertools import groupby

ventas = {
    "Enero": 15000,
    "Febrero": 12000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000
}


def agrupar(ventas):
    lista = []
    for key, value in ventas.items():
        lista.append(value)

    lista.sort()

    return {key: len(list(value)) for key, value in groupby(lista)}


agrp = agrupar(ventas)

# for key, value in agrp.items():
#     print(key, value)
