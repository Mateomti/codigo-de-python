# Crea una clase Calculadora con un método de clase
# llamado suma que acepte dos números como argumentos y devuelva
# la suma de ellos.
# Luego, utiliza este método para realizar
# algunas operaciones de suma.
class Calculadora():
    def Suma(self):
        a = int(input('Ingrese el primer numero a sumar: '))
        b = int(input('Ingrese el segundo numero a sumar: '))
        res = a+b
        print(f'El resultado es: {res}')

x = Calculadora()
x.Suma()