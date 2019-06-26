from sys import argv

precio = float(argv[1])
numUsuarios = int(argv[2])
gastos = float(argv[3])

utilidades = precio*numUsuarios-gastos

# print("Utilidades brutas")
# print(utilidades)

if utilidades > 0:
    utilidades = utilidades*0.65

# print("Utilidades netas")
print (utilidades)
