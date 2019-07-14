from sys import argv

numero1 = int(argv[1])
numero2 = int(argv[2])
numero3 = int(argv[3])

if numero1 > numero2 and numero1 > numero3:
    print(numero1)
elif numero2 > numero3:
    print(numero2)
else:
    print(numero3)