# Crea un programa que solicite un número entero al usuario y determine
# si es un número negativo, positivo o igual a cero.
# En caso de ser positivo, verifica si es par o impar.

x = int(input("Ingrese un numero entero: "))

if x == 0:
    print("El numero es cero.")
elif x > 0:
    print("Numero positivo.")
    if x % 2 == 0:
        print("Ademas el numero es par.")
    else:
        print("Ademas el numero es impar.")
else:
    print("Numero negativo.")
