def letra_o(ancho):
    salida = ''
    lineasExtremas = '*'*ancho
    lineasMedias = '*' + ' ' * (ancho-2) + '*' + '\n'
    salida = lineasExtremas + '\n'
    for i in range(ancho-2):
        salida = salida + lineasMedias
    salida = salida + lineasExtremas
    return salida


print(letra_o(5))
