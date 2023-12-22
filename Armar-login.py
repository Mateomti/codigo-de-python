base = {}

def registrar():
    usuario = input('Ingrese su nombre de usuario: ')
    contrasena = input('Inrgese su contraseña: ')
    base[usuario] = contrasena
    print("Usted ha sido registradop correctamente!")

def mostrar():
    for key, value in base.items():
        print(f'Usuario: {key}, Contraseña: {value}.')

def login(usu,contra):
    for keys, values in base.items():
        if keys != usu:
            print('Usuario no encontrado.')
        elif  values != contra:
            print("Contraseña incorrecta.")
        else:
            print('Bienvenido!')
            break

while True:
    op = input('''\nMenu de opciones
    1- Registrar usuario y contraseña.
    2- Revisar todos los usuarios.
    3- Loguear usuario.
    0- Salir.
    Ingrese una opcion: ''')
    if op == '1':
        registrar()
    elif op == '2':
        print('Usuarios y contraseñas registradas en el sistema: ')
        mostrar()
    elif op == '3':
        u = input('Ingrese su usuario: ')
        c = input('Ingrese su contraseña: ')
        login(u,c)
    elif op == '0':
        print('Hasta luego!')
        break
    else:
        print('Opcion invalida.')