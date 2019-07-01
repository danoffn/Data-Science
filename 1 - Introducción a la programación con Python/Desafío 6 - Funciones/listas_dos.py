from velocidad import promedio
from listas_uno import autos

# def getLista(autos, indice)
#     for index, valor in enumerate(autos):
#         # print(autos[index][indiceVelocidad])
#         lista.append(autos[index][indiceVelocidad])
#         return lista


def promedio_velocidad(autos, indiceVelocidad):
    largo = len(autos)
    lista = []
    for index, valor in enumerate(autos):
        # print(autos[index][indiceVelocidad])
        lista.append(autos[index][indiceVelocidad])
    return promedio(lista)

print(promedio_velocidad(autos, 1))
print(promedio_velocidad(autos, 2))
print(promedio_velocidad(autos, 4))