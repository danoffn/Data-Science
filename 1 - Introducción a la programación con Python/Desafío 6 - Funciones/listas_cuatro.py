from listas_uno import autos
from velocidad import promedio

def getAutos(autos, indice):
    lista = []
    # return promedio
    for index, valor in enumerate(autos):
        # print(autos[index][indiceVelocidad])
        if autos[index][3] is True:
            lista.append(autos[index][0])

    return lista


def imprimir(lista):
    for valor in lista:
        print(valor)


imprimir(getAutos(autos, 1))
