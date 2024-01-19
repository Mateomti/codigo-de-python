# Escribe un programa que tome una lista de palabras ingresadas por el usuario.
# Luego, que muestre cada palabra una por una.
# Si la palabra es "salir", finaliza el programa.
# Si la palabra es "omitir", se pasa a la siguiente iteración.
# Al final, si ninguna palabra fue "salir", muestra un mensaje avisando la situación.


lista = input("Ingrese una lista de palabras: ").split()

for n in lista:
    if n == 'salir':
        print("Se ha encontrado la palabra 'salir', finalizando el programa.")
        break
    elif n == 'omitir':
        continue
    else:
        print(n)
else:
    print("No se ha encontrado la palabra salir.")
