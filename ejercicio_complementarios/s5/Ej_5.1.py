# Crea un programa que permita a un usuario llevar un registro de tareas pendientes. El programa debe:
# Permitir al usuario agregar tareas.
# Marcar tareas como completadas. agregámdole un tilde o algo que identifique que se completó al principio de la tarea.
# Listar las tareas pendientes.

tareas = {}


def crear_tarea():
    t = input("Ingrese la tarea a realizar: ")
    tareas[t] = 'Incompleta'


def actualizar_tarea(t):
    tareas[t] = '✔'


def listar():
    for tarea, estado in tareas.items():
        # if estado not == '✔':
        print(f"{str(tarea).capitalize()}: {str(estado).capitalize()}.")


while True:
    op = input('''\nMenu de opciones
1- Crear una tarea.
2- Actualizar una tarea.
3- Listar tareas.
0- Salir.
Ingrese una opcion: ''')

    if op == '1':
        crear_tarea()

    elif op == '2':
        t = input("Ingrese el nombre de la tarea que desea actualizar: ")
        while t not in tareas:
            t = input("Ingrese una tarea existente: ")
        actualizar_tarea(t)

    elif op == '3':
        listar()

    elif op == '0':
        print("Cerrando aplicacion. Hasta luego!")
        break

    else:
        print("Opcion invalida, reintente.")
