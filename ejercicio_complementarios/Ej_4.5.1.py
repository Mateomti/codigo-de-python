# Imagina que estás administrando un pequeño almacén y deseas realizar
# un seguimiento de los productos en tu inventario.

# Escribe un programa que te permita ingresar el nombre y la cantidad de varios productos.
# Utiliza un bucle para recorrer los productos y mostrar su nombre y cantidad.
# Al final, muestra el total de productos en el inventario.
produ = {}
cp = 0

while True:

    produ.update({input("Ingrese el nombre del producto: ")
                 : int(input("Ingrese la cantidad: "))})

    if input("Desea ingresar un nuevo producto? Si o no: ") == 'no':
        print("\n")
        break

for key, value in produ.items():
    print(f"Producto: {key}, cantidad: {value}")
    cp += value
print(f"La cantidad total de productos es: {cp}")
