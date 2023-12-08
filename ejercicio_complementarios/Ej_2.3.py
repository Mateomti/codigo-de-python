# Crea un programa que tome una oración ingresada por el usuario y realice las siguientes operaciones:
#   convierte la oración a mayúsculas,
#   cuenta cuántas veces aparece la palabra "python",
# y muestra la oración sin espacios en blanco al inicio y al final.


x = input("Ingrese una oracion: ")

print(f"Oracion a mayusculas: {x.upper()}")

print(f"Cantidad de veces que aparece la palabra 'python': {
      x.lower().count('python')}")

print(f"Oracion sin los espacios en blancos: {x.strip()}")
