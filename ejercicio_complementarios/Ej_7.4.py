# Crea una clase Libro con atributos de instancia como
# titulo, autor, año_publicacion,y disponible (un valor booleano).
# Luego, crea una clase Biblioteca que tenga una lista
# de libros y métodos de instancia para prestar un libro,
# devolver un libro y mostrar todos los libros disponibles.
# Utiliza atributos de clase para registrar la cantidad
# total de libros en la biblioteca. Crea instancias de ambas
# clases y realiza operaciones de préstamo y devolución de libros.
class Libro():
    def __init__(self,titulo, autor, ap) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ap = ap
        self.estado = True
    def __str__(self) -> str:
        return f'''Titulo: {self.titulo}
Autor: {self.autor}
Año de publicacion: {self.ap}
Disponibilidad: {self.estado}'''

class Biblioteca():
    cl = 0
    def __init__(self) -> None:
        self.libros = []
    def agregar_libro(self, *args):
        self.libros.append(args)
        for _ in args:
            self.cl += 1
    def prestar_libro(self, titulo):
        # for i,libro in self.libros:
        #     if self.libros[i].titulo == titulo and libro.estado:
        #         libro.estado = False
        #     else:
        #         print('El libro ya ha sido prestado.')
        pass
    def devolver_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and libro.estado is False:
                libro.estado = True
            else:
                print('El libro ya estaba en la biblioteca')
    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)

libro1 =  Libro('Enero', 'Mateo', 2022)
libro2 =  Libro('Sape', 'Bananero', 2002)

biblioteca = Biblioteca()

biblioteca.agregar_libro(libro1, libro2)
print(f'La cantidad de libros en la biblioteca es de: {biblioteca.cl}')
biblioteca.prestar_libro('Enero')
biblioteca.mostrar_libros()
biblioteca.devolver_libro('Sape')
biblioteca.devolver_libro('Enero')
biblioteca.mostrar_libros()
