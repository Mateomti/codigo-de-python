# Crear un programa que muestre un menu con 4 opciones y,
# segun la opcion elegida por el usuario, muestre el tipo de error
# que se generaria si se ejecutara ese codigo en python.
# Usa las siguientes opciones:
# 1. "Soy un string" - 4
# 2. 4/0
# 3. prnt("Mostrando codigo")
# 4. int("Quiero ser un numero")

while True:
    op = input('''Usa las siguientes opciones:
    1. "Soy un string" - 4
    2. 4/0
    3. prnt("Mostrando codigo")
    4. int("Quiero ser un numero")
    0. Salir
    Ingrese una opcion: ''')
    try:
        if op == '1':
            "Soy un string" - 4
        elif op == '2':
            print(f"El error seria el siguiente: {ZeroDivisionError.__name__}")
        elif op == '3':
            prnt("Mostrando codigo")
        elif op == '4':
            int("Quiero ser un numero")
        elif op == '0':
            break
    except Exception as e:
        print(f"El error seria el siguiente: {type(e).__name__}")