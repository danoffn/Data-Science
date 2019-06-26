entrada = input("Ingresa contraseña\n")
entrada = entrada.lower()

suma = 0
for letra in entrada:
    for j in range(ord('a'), ord(letra)+1):
        suma = suma+1

print(str(suma) + ' intentos')
