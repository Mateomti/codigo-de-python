# Crea un programa que solicite al usuario ingresar una palabra.
# Luego, recorre la palabra y cuenta cuántas vocales contiene.
# Al final, si no se encontraron vocales, muestra un mensaje
# comunicando que la palabra ingresada solo contiene consonantes.

palabra = input("Ingrese una palabra: ")
cv = 0
for letra in palabra:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        cv += 1
if cv == 0:
    print("La palabra solo contiene consonantes.")
else:
    print(f"La palabra contiene {cv} vocales.")
