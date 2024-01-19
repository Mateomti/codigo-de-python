# Escribe un programa que tome un número entero positivo
# ingresado por el usuario y muestre la tabla de multiplicar de ese número.
# Repite la solicitud al usuario de ingresar un nuevo número hasta que ingrese un cero.

while True:
    num = int(input(
        "Ingrese un numero entero positivo para empezar o un cero para finalizar: "))
    while num < 0:
        num = int(input("El numero debe ser positivo o cero, reintente: "))
    if num == 0:
        print("Finalizando el programa.")
        break
    print(f"La tabla de multiplicar de {num} es:")
    for numero in range(0, num*11, num):
        print(numero)
