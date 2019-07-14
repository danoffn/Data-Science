ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}


def cuartos(diccionario, meses_trimestre, clave_trimestre):
    quarters = {}
    quarters[clave_trimestre] = 0
    for clave, valor in diccionario.items():
        for valorLista in meses_trimestre:
            if clave == valorLista:
                quarters[clave_trimestre] = quarters[clave_trimestre] + valor
    return quarters


def JoinCuartos(diccionario):
    Q1 = {}
    Q2 = {}
    Q3 = {}
    Q4 = {}

    Q1 = cuartos(ventas, ["Enero", "Febrero", "Marzo"], "Q1")
    Q2 = cuartos(ventas, ["Abril", "Mayo", "Junio"], "Q2")
    Q3 = cuartos(ventas, ["Julio", "Agosto", "Septiembre"], "Q3")
    Q4 = cuartos(ventas, ["Octubre", "Noviembre", "Diciembre"], "Q4")

    Q1.update(Q2)
    Q1.update(Q3)
    Q1.update(Q4)

    return Q1


# nuevoDict = cuartos(ventas, ["Enero", "Febrero", "Marzo"], "Q1")

quarters = JoinCuartos(ventas)

# for key, value in quarters.items():
#     print(key, value)

print(quarters)