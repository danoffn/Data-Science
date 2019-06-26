numero1 = int(input("Ingrese un número para comenzar la busqueda de pares\n"))

for i in range(1, numero1+1):
    if i % 2 == 0:
        print(i)
