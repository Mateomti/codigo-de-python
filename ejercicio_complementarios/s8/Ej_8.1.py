from datetime import datetime


def registrar_gasto():
    d = input('Ingrese la descripccion: ')
    c = input('Ingrese la cantidad: ')
    factual = datetime.now()
    aa = open('Registro de gastos.txt', 'a')
    aa.write(f'Fecha: {factual} - Descripción: {d} - Cantidad: {c}\n')
    aa.close()

while True:
    op = input(
'''******* MENU DE OPCIONES *******
1- Registrar gasto
2- Salir
Ingrese una opcion: ''')
    if op == '1':
        registrar_gasto()
    elif op == '2':
        print('Hasta luego!!')
    else:
        print('Opcion invalida.')