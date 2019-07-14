# from velocidad import promedio
from listas_uno import autos
from velocidad import promedio
from listas_dos import promedio_velocidad


def mayorPromedio(autos, indice):
    lista = []
    promedio = promedio_velocidad(autos, indice)
    # return promedio
    for index, valor in enumerate(autos):
        # print(autos[index][indiceVelocidad])
        if autos[index][indice] > promedio:
            lista.append(autos[index][0])

    return lista


def imprimir(lista):
    for valor in lista:
        print(valor)


imprimir(mayorPromedio(autos, 1))
