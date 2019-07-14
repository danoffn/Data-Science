from sys import argv

precio = float(argv[1])
numUsuarios = int(argv[2])
numUsuariosPremium = int(argv[3])
numUsuariosGratuitos = int(argv[4])
gastos = float(argv[5])

# print("precio: " + str(precio))
# print("numUsuarios: " + str(numUsuarios))
# print("numUsuariosNormales: " + str(numUsuariosNormales))
# print("numUsuariosPremium: " + str(numUsuariosPremium))
# print("numUsuariosGratuitos: " + str(numUsuariosGratuitos))
# print("gastos: " + str(gastos))

utilidades = 2*precio*numUsuariosPremium-gastos

# print("Utilidades brutas")
# print(utilidades)

if utilidades > 0:
    utilidades = utilidades*0.65

# print("Utilidades netas")
print(int(utilidades))
