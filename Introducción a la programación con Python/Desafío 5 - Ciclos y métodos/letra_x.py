# def letra_x(ancho):
#     N = ancho
#     for i in range(N):
#         for j in range(N):
#             if (i == j) or ((N - j - 1) == i):
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#         print('')


def letra_x(ancho):
    N = ancho
    salida = ''
    for i in range(N):
        linea = ''
        for j in range(N):
            if (i == j) or ((N - j - 1) == i):
                linea = linea + "*" 
            else:
                linea = linea + ' '
        # print(linea)
        salida = salida + linea + '\n'
    return salida


# letra_x(10)
