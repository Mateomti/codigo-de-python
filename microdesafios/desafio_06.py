# En la función de nuestro ejercicio hay un fallo potencial (aritmético),
# averigua cuándo sucede y retorna el valor None en ese caso especial,
# en cualquier otro caso devuelve el resultado normal de la función.

def dividir(a, b):

    print('El programa funciono correctamente.')
    print(a/b)


try:
    dividir(int(input('Ingrese un numero: ')),
            int(input('Ingrese otro numero: ')))
except ValueError:
    print(None)

