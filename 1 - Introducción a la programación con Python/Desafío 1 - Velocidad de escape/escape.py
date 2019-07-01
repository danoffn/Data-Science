from sys import argv
gravedad = float(argv[1])
radio = float(argv[2])

#print (gravedad)
#print (radio)
radio = radio*1000

velocidad = (2*gravedad*radio)**(1/2)
velocidad = round(velocidad, 3)
print(velocidad)
