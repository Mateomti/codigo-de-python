# Crea un programa que solicite dos números enteros al usuario y determine si ambos son números pares.

x = int(input("Ingrese un numero: "))
y = int(input("Ingrese otro numero: "))

if x % 2 == 0 and y % 2 == 0:
    print("Ambos numeros son numeros pares.")
else:
    print("Alguno de los numeros no es un numero par.")
