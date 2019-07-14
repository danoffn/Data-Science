from sys import argv

precio = float(argv[1])
numUsuarios = int(argv[2])
gastos = float(argv[3])

if len(argv) == 5:
    utilidadesAnoAnterior = float(argv[4])
else:
    utilidadesAnoAnterior = 1000

# print("precio: " + str(precio))
# print("numUsuarios: " + str(numUsuarios))
# print("gastos: " + str(gastos))
# print("utilidades año anterior: " + str(utilidadesAnoAnterior))

utilidades = precio*numUsuarios-gastos

# print("Utilidades brutas año actual")
# print(utilidades)

if utilidades > 0:
    utilidades = utilidades*0.65

# print("Utilidades netas")
# print (utilidades)

# print("Suma utilidades")
print(utilidades + utilidadesAnoAnterior)
