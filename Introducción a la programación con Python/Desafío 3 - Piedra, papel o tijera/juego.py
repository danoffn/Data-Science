from sys import argv
import random

jugadaEntrada = argv[1].lower()

if jugadaEntrada != "piedra" and jugadaEntrada != "papel" and jugadaEntrada != "tijera":
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
    exit()

jugadaComputador = random.choice(['piedra', 'papel', 'tijera'])

print("Computador juega " + jugadaComputador)

if jugadaEntrada == jugadaComputador:
    print("Empataste")
elif jugadaEntrada == "piedra" and jugadaComputador == "papel":
    print("Perdiste")
elif jugadaEntrada == "piedra" and jugadaComputador == "tijera":
    print("Ganaste")
elif jugadaEntrada == "papel" and jugadaComputador == "tijera":
    print("Perdiste")
elif jugadaEntrada == "papel" and jugadaComputador == "piedra":
    print("Ganaste")
elif jugadaEntrada == "tijera" and jugadaComputador == "piedra":
    print("Perdiste")
elif jugadaEntrada == "tijera" and jugadaComputador == "papel":
    print("Ganaste")
