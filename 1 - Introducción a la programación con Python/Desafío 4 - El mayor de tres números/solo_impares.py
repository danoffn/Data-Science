numero1 = int(input("Ingrese un número para comenzar la busqueda de impares\n"))

for i in range(numero1+1):
    if i % 2 != 0:
        print(i)
