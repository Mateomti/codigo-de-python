# Define una clase Figura con un método de instancia
# area que devuelve el área de la figura.
# Luego, crea clases hijas como Circulo y Rectangulo
# que hereden de Figura y proporcionen implementaciones diferentes del método area.
class Figura:
    """clase padre, figura
    """
    def area(self):
        ...


class Circulo(Figura):
    """clase circulo
    """
    def __init__(self) -> None:
        self.radio = int(input('Ingrese el radio del circulo: '))**2
    def area(self):
        return 3.1415 * self.radio

class Triangulo(Figura):
    """clase triangulo
    """
    def __init__(self) -> None:
        self.altura = int(input('Ingrese la altura del triangulo: '))
        self.base = int(input('Ingrese la base del triangulo: '))
    def area(self):
        return (self.base * self.altura) / 2

while True:
    try:
        op = input(
    '''Ingrese que elemento quiere crear y calcular su area:
        1. Circulo.
        2. Triangulo.
        0. Salir
        Opcion: ''')
        if op == '1':
            c = Circulo()
            print(f'El area del circulo es: {c.area()}')
        elif op == '2':
            t = Triangulo()
            print(f'El area del triangulo es: {t.area()}')
        elif op == '0':
            print('hasta luego!')
            break
        elif op in 'qwertyuiopasdfghjklñ<zxcvbmn':
            raise TypeError
        elif 0 > int(op) > 2:
            raise ValueError
        else:
            print('Opcion invalida.')
    except ValueError:
        print(f'Ha ocurrido un error: {ValueError.__name__}')
    except TypeError:
        print(f'Ha ocurrido un error: {TypeError.__name__}')
    except Exception as e:
        print(f'Ha ocurrido un error desconocido: {type(e).__name__}')
