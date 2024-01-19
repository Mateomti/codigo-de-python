# Imagina que estás administrando un pequeño almacén y deseas realizar
# un seguimiento de los productos en tu inventario.

# Escribe un programa que te permita ingresar el nombre y la cantidad de varios productos.
# Utiliza un bucle para recorrer los productos y mostrar su nombre y cantidad.
# Al final, muestra el total de productos en el inventario.

n = int(input("Ingrese la cantidad de articulos que va a agregar: "))

inventario = {}
cp = 0
i = 0

while i < n:
    i += 1
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    inventario[nombre] = cantidad

for key, value in inventario.items():

    print(f"Producto: {key}, cantidad: {value}")
    cp += value

print(f"Cantidad total de productos: {cp}")
