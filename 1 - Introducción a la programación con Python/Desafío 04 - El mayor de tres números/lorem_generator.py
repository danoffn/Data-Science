from sys import argv

entrada = int(argv[1])

lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque vel cursus augue, et iaculis neque. Etiam vestibulum justo eget ligula tincidunt, volutpat finibus magna blandit. Cras ut erat mi. Curabitur malesuada aliquam pellentesque. Curabitur a justo a lectus faucibus sagittis vitae sed erat. Aliquam neque tellus, convallis cursus turpis eu, elementum eleifend urna. Donec convallis erat a libero ornare, at tincidunt diam sodales. Phasellus ornare odio in orci pretium, sed vehicula nulla cursus. Pellentesque mattis semper tincidunt. Nunc cursus lacus eget nunc eleifend, eu consequat dui scelerisque. Suspendisse interdum nibh vitae diam convallis, vel volutpat dui scelerisque. Fusce dapibus leo quis ante ullamcorper, quis efficitur mi aliquet. Mauris ac tellus efficitur nisi auctor tincidunt quis a turpis. Duis nec dignissim erat. Etiam egestas sem vitae ligula tempor molestie. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.'

for i in range(entrada):
    print(lorem)
    if i < entrada-1:
        print()
