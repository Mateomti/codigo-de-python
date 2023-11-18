print("Bienvenido a la calculadora.")
print("Para salir escribe \"salir\". ")
print("Se pueden realizar cuatro operaciones: suma, resta, multi, div")

n1 = None
while True:

    if n1 is None:
        n1 = int(input("Ingrese el primero numero: "))

    op = input("Ingrese una operacion: ")

    if "salir" in op:
        break

    n2 = int(input("Ingrese el segundo numero: "))

    if op.lower() == "suma":
        n1 += n2
        print(n1)

    elif op.lower() == "resta":
        n1 -= n2
        print(n1)

    elif op.lower() == "multi":
        n1 *= n2
        print(n1)

    else:
        n1 /= n2
        print(n1)
