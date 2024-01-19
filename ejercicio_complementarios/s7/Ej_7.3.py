#Crea una clase Empleado que tenga los siguientes atributos de instancia:
# nombre, apellido, edad, salario.
# Luego, crea una clase Gerente que herede de Empleado y tenga
# un atributo adicional departamento. Define métodos de instancia
# para ambas clases, como mostrar_informacion para mostrar los
# detalles de un empleado y aumentar_salario para aumentar el
# salario de un empleado en un porcentaje dado.
# Crea instancias de ambas clases y realiza algunas operaciones.
class Empleado():
    
    def __init__(self) -> None:
        self.nombre = input('Ingrese el nombre: ')
        self.apellido = input('Ingrese el apellido: ')
        self.edad = int(input('Ingrese el edad: '))
        self.salario = int(input('Ingrese el salario: '))
        
    def mostrar_informacion(self):
        self.__str__()
        
    def aumentar_salario(self):
        por = int(input('Ingrese el porcentaje en el que desea aumentar el salario: '))
        self.salario += (self.salario * por) / 100
        
    def __str__(self) -> str:
        return f"""\nNombre: {self.nombre}
Apellido: {self.apellido}
Edad: {self.edad}
Salario: {self.salario}"""

class Gerente(Empleado):
    def __init__(self) -> None:
        super().__init__()
        self.departamento = input('Ingrese el departamento del gerente: ')
    def __aux__(self) -> None:
        print('Empleado encontrado.')
    def __str__(self) -> str:
        return f"""\nNombre: {self.nombre}
Apellido: {self.apellido}
Edad: {self.edad}
Salario: {self.salario}
Departamento: {self.departamento}"""

vector = []
x = int(input('Ingrese la cantidad de empleados a registrar: '))

for i in range(0, x):
    n = len(vector)
    op = input('''
Ingrese que tipo de empleado quiere ingresar:
1- Empleado comun.
2- Gerente.
Opcion: ''')
    if op == '1':
        e = Empleado()
        
        vector.insert(n, e)
    elif op == '2':
        g = Gerente()
        vector.insert(n, g)
    elif op != 1 or op != 2:
        raise ValueError

while True:
    op = input('''\n
******* MENU DE OPCIONES *******
1- Ver informacion de todos los empleados comunes.
2- Ver informacion de todos los gerentes.
3- Aumentar el salario a un empleado.
0- Salir.
Opcion: ''')
    if op == '1':
        for i, v in enumerate(vector):
            if type(v).__name__ == 'Empleado':
                print(vector[i])
    elif op == '2':
        for i, v in enumerate(vector):
            if type(v).__name__ == 'Gerente':
                print(vector[i])
    elif op == '3':
        bus = input('Ingrese el apellido del empleado al que le quiere aumentar el salario: ')
        for i, v in enumerate(vector):
            if bus in vector[i].apellido:
                v.aumentar_salario()
    elif op == '0':
        print('Hasta luego!')
        break
    else:
        print('Opcion Invalida.')