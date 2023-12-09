# Escribe un programa que lea un número impar por teclado.
# Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

while True:
    numero = int(input("Ingrese un numero: "))

    if numero % 2 == 0:
        print("El numero es par. Finalizando el programa.")
        break
    else:
        print("El numero no es par, intente de nuevo.")
