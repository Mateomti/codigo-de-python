#Escribe un programa que permita al usuario ingresar su edad.
# El programa debe validar si la edad ingresada
# está dentro del rango de 18 a 65 años, y mostrar un mensaje correspondiente.
# Utiliza un bloque try-except con múltiples bloques except
# para manejar posibles errores relacionados con la entrada del usuario,
# como una entrada no numérica o una edad fuera del rango válido.
while True:
    try:
        edad = int(input('Ingrese su edad: '))
        if 18 <= edad <= 65:
            print('Su edad se encuentra dentro del rango de 18 a 65 años.')
            break
        elif edad <= 0:
            raise ValueError()
        else:
            raise ValueError()
    except TypeError:
        print(f'ERROR. Se ha ingresado un dato de tipo string: {TypeError.__name__}')
    except ValueError:
        print(f'ERROR. Se ha ingresado un valor invalido: {ValueError.__name__}')
    except Exception as e:
        print(f'ERROR. Se ha generado un error desconocido: {type(e).__name__}')