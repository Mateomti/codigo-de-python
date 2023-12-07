# Escribe un programa que tome un número entero ingresado por el usuario
# y determine si es un número par, divisible por 3 y 5 al mismo tiempo, o ninguno de los anteriores.

x = int(input("Ingrese un numero: "))

if x % 2 == 0 and x % 3 == 0 and x % 5 == 0:
    print("El numero es valido.")
else:
    print("El numero no es valido")
