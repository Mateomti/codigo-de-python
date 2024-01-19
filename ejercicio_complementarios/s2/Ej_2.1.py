# Crea un programa que solicite al usuario ingresar nombres separados por comas.
# Luego, crea un conjunto con los nombres ingresados y
# muestra por pantalla la cantidad de nombres únicos en el conjunto.

nombres = input("Ingrese una serie de nombres todos separados por comas: ")

set_nombres = set(nombres.split(', '))

print(set_nombres)
