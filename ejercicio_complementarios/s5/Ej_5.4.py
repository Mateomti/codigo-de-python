# Crea un programa que permita calcular el promedio de un número variable de notas ingresadas por el usuario.
# La función calcular_promedio puede recibir un número variable de notas.
# Luego, muestra el promedio de las notas ingresadas.
def calcular_promedio(*notas):
    res = sum(notas)
    promedio = res / len(notas)
    print(f'El promedio es {promedio}')


notas = []
while True:
    nota = float(input('Ingrese una nota o -1 para finalizar: '))
    if nota == -1:
        break
    notas.append(nota)

if notas:
    calcular_promedio(*notas)
else:
    print('No se han ingresado notas.')
