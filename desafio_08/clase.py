class Alumno():
    def __init__(self, nombre, nota) -> None:
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print(f"Nombre: {self.nombre}, nota: {self.nota}")