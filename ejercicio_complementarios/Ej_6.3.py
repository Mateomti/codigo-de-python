#Escribe un programa que permita al usuario ingresar el precio de un producto y un código de descuento.
# El programa debe validar si el precio es un número positivo y si el código
# de descuento es válido. Los errores posibles incluyen entradas no numéricas,
# números negativos y códigos de descuento no válidos.
#Los codigos de descuento son:
descuentos_validos = ["DESC10", "DESC20", "DESC30"]

while True:
    try:
        precio = int(input('Ingrese el precio del producto o 0 para finalizar: '))
        if precio < 0:
            raise ValueError
        elif precio == 0:
            print('Hasta luego!')
            break
        else:
            print('Precio valido.')
        descuento = input('Ingrese un codigo de descuento: ')
        if descuento.upper() not in descuentos_validos:
            raise TypeError
        elif descuento.upper() == 'DESC10':
            print(f'Descuento valido. Precio final: {precio - (precio/10)}')
        elif descuento.upper() == 'DESC20':
            print(f'Descuento valido. Precio final: {precio - (precio/20)}')
        elif descuento.upper() == 'DESC30':
            print(f'Descuento valido. Precio final: {precio - (precio/30)}')
    except ValueError:
        print('ERROR. El precio ingresado no es valido.')
    except TypeError:
        print('El string ingresado no es valido.')