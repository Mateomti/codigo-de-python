# Crea un programa que simule un inventario de productos en una tienda.
# Inicia con un diccionario que contenga algunos productos y sus cantidades.
# Luego, permite al usuario agregar un nuevo producto con su cantidad y actualizar
# la cantidad de un producto existente.
# Muestra el inventario actualizado.

inventario = {'manzanas': 50, 'bananas': 30, 'peras': 40}

inventario.update({input("Ingrese la fruta que desea agregar: ")                  : int(input("Ingrese la cantidad: "))})

inventario.update({input(f"Indique de que fruta quiere cambiar la cantidad({inventario.keys()}): "): int(
    input("Indique la nueva cantidad: "))})

print(inventario)
