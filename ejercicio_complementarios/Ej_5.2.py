# Desarrolla un programa que permita a un usuario registrar
# información de contactos (nombre, número de teléfono y correo electrónico).
# El programa debe almacenar estos contactos y permitir
# al usuario buscar contactos por nombre o número de teléfono.
contactos = {}


def reg_contactos(nombre, telefono, correo):
    contactos[nombre] = {'telefono': telefono, 'correo': correo}


def buscar_contacto(bus):
    for key, value in contactos.items():
        if str(bus).lower() == str(key).lower() or bus == value['telefono']:
            print(f'Nombre del contacto: {key}')
            print(f'Telefono: {value['telefono']}')
            print(f'Correo: {value['correo']}')


while True:
    op = input('''Menu de opciones
    1- Registrar un contacto.
    2- Buscar un contacto.
    0- Salir.
    Ingrese una opcion: ''')

    if op == '1':
        n = input('Ingrese el nombre del contacto: ')
        t = input('Ingrese su numero de telefono: ')
        c = input('Ingrese su correo: ')
        reg_contactos(n, t, c)
    elif op == '2':
        n = input('Ingrese el nombre del contacto a buscar o su telefono: ')
        buscar_contacto(n)
    elif op == '0':
        print('Hasta luego!')
        break
    else:
        print("Ingrese una opcion valida.")
