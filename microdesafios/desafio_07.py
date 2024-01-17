#Desafío 07
#Crea una clase Auto que contenga 2 atributos de instancia.
#Con esa clase, crea un auto y muestra los datos del auto creado.
class auto:
    ruedas = 4
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

auto1 = auto('toyota','rojo')
auto2 = auto('hyundai', 'amarillo')
print(f'marca: {auto1.marca}, color: {auto1.color}, ruedas: {auto1.ruedas}')
print(f'marca: {auto2.marca}, color: {auto2.color}, ruedas: {auto2.ruedas}')