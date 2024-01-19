# # El total o exit?
# Solicitar al usuario la cantidad de numeros enteros a sumar.
# Luego permitirle ingresarlos uno por uno hasta que se ingresen todos o el usuario escriba la palabra 'exit'.
# El programa debe validar que se ingreso 'exit' y dejar de solicitar numeros.
# Finalmente, el algoritmo debe mostrar la suma obtenida con un mensaje
# que resalte si fue total la carga de datos o parcial (debido al ingreso de 'exit').

n = int(input("Ingrese la cantidad de numeros enteros a sumar: "))
i = 0
res = 0
while i < n:
    i += 1
    op = input("Ingrese el numero a sumar o la palabra exit para salir: ")
    if op == 'exit':
        print(
            f'Terminando el programa, el ingreso de datos fue parcial, y el resultado obtenido fue {res}.')
        break
    elif op in '1234567890':
        res += int(op)
    else:
        print("Opcion invalida, reintente.")
else:
    print(f'El resultado total fue: {res}')
