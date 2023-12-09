# Escribe un programa que tome una lista de nombres ingresados
# por el usuario separados por un espacio y los liste mostrando su ubicacion.

nombre = input("Ingrese una serie de nombres separados por un espacio: ")

lista = nombre.split(' ')

for i, n in enumerate(lista):
    print(f"Nombre: {n} \nIndice: {i}")
