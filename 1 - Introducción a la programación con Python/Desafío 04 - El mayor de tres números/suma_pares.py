numero1 = int(input("Ingrese un número para comenzar suma de pares\n"))

suma = 0
linea = ''
for i in range(1, numero1+1):
    if i % 2 == 0:
        suma = suma + i
        linea = linea + str(i)
        if i != numero1:
            linea = linea + '+'

# print(linea + '\n')
print(suma)
