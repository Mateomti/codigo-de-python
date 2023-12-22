# Crea un programa que permita a un usuario configurar la red de una computadora.
# El programa debe aceptar argumentos clave para configurar
# la dirección IP, la máscara de subred y la puerta de enlace.
# Luego, muestra la configuración de red completa.
red = {}


def config(**kwargs):
    red[ip] = {'mascara de subred': ms,
                'puerta de enlace': pe}


def mostrar():
    for key, value in red.items():
        print(f'''    IP: {key}
    Mascara de subred: {value['mascara de subred']}
    Puerta de enlace: {value['puerta de enlace']}\n''')


while True:
    op = input('''Menu de opciones
    1- Configurar red.
    2- Ver configuracion actual.
    0- Salir.
    Ingrese una opcion: ''')
    if op == '1':
        ip = input('Indique la direccion IP: ')
        ms = input('Ingrese la mascara de subred: ')
        pe = input('Ingrese la puerta de enlace: ')
        config(ipe=ip, mascara=ms, puerta=pe)
    elif op == '2':
        mostrar()
    elif op == '0':
        print('Hasta luego!')
        break
    else:
        print('Opcion invalida, reintente\n')
