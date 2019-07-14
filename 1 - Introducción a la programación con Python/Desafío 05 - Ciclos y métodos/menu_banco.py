def mostrar_menu(saldo=0):

    while(True):
        print('Bienvenido al portal del Banco Amigo. Escoja una opción:')
        print('1. Consultar saldo')
        print('2. Hacer depósito')
        print('3. Realizar giro')
        print('4. Salir')
        entrada = int(input())

        if entrada == 1:
            print(getSaldo(saldo))
        elif entrada == 2:
            cantidad = int(input("Ingrese cantidad a depositar\n"))
            saldo = depositar(saldo, cantidad)
            print(getSaldo(saldo))
        elif entrada == 3:
            if saldo <= 0:
                print("No se puede girar esta cantidad. " + getSaldo(saldo))
            else:
                cantidad = int(input("Ingrese cantidad a girar\n"))
                resultado = girar(saldo, cantidad)
                if resultado is False:
                    print("No se puede girar esta cantidad. " + getSaldo(saldo))
                else:
                    saldo = resultado
                    print(getSaldo(saldo))
        elif entrada == 4:
            break


def depositar(saldo, cantidad):
    return saldo + cantidad


def girar(saldo, cantidad):
    if cantidad <= saldo:
        return saldo - cantidad
    else:
        return False


def getSaldo(saldo):
    return "Su saldo es de " + str(saldo)

mostrar_menu(1000)