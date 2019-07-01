from velocidad import promedio
from listas_uno import autos


def getArray(lista, indiceCol):
    lista = []
    for index, valor in enumerate(autos):
        lista.append(float(autos[index][indiceCol]))
    return lista


lista = getArray(autos, 1)
prom = promedio(lista)

resp = list(filter(lambda x: x > prom, lista))
print(resp)
