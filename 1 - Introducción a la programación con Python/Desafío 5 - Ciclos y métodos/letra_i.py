def letra_i(ancho):
    lineasExtremas = '*'*ancho + '\n'
    if ancho % 2 == 0:
        lineasMedias = ' ' * (int(ancho/2)-1) + '*' + ' ' * (int(ancho/2)-1) + '\n'
    else:
        lineasMedias = ' ' * (int(ancho/2)) + '*' + ' ' * (int(ancho/2)-1) + '\n'

    salida = lineasExtremas
    for i in range(ancho-2):
        salida = salida + lineasMedias
    salida = salida + lineasExtremas

    return salida

    
# letra_i(10)
