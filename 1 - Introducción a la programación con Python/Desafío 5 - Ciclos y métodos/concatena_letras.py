def gen(numeroLetras):
    if numeroLetras > ord('z')-ord('a'):
        numeroLetras = ord('z')-ord('a')+1

    cadena = ''
    for j in range(ord('a'), ord('a') + numeroLetras):
        cadena = cadena + chr(j)
    return cadena
