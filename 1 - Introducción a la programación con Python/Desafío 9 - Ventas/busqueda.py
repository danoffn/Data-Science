from sys import argv

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

# entradas = []

entradas = (argv[1:])
entradas = [float(entrada) for entrada in entradas]

# for entrada in entradas:
#     print(str(entrada))

ventas_inv = {value: key for key, value in ventas.items()}

for entrada in entradas:
    if entrada in ventas_inv:
        print(ventas_inv[entrada])
    else:
        print("no encontrado")
