# Escribe una función a la que se le pase una cadena
# del nombre de una ciudad <ciudad> y muestre por pantalla
# el saludo ¡¡Hola, te damos la bienvenida a <ciudad>!.

def bienvenida(ciudad):
    print(f'¡¡Hola, te damos la bienvenida a {ciudad}!!.')


bienvenida(input("Ingrese una ciudad: "))
