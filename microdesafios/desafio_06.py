# En la función de nuestro ejercicio hay un fallo potencial (aritmético),
# averigua cuándo sucede y retorna el valor None en ese caso especial,
# en cualquier otro caso devuelve el resultado normal de la función.

def dividir(a, b):

    return a/b


try:
    print(dividir(5,'6'))
except:
    print(None)

