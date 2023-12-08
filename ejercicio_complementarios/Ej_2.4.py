# Crea dos conjuntos con números ingresados por el usuario y separados por coma.
# Luego, muestra cuáles elementos tienen en común los conjuntos y crea un nuevo conjunto que contenga la unión de ambos.

set1 = set(input("Ingrese una serie de numeros separados por coma: ").split(', '))

set2 = set(input("Ingrese otra serie de numeros separados por coma: ").split(', '))

print(f"Conjunto 1: {set1}")
print(f"Conjunto 2: {set2}")
print(f"Elementos que tiene en comun: {set1.intersection(set2)}")
