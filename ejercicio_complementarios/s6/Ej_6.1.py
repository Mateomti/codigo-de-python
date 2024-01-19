# Desarrolla un programa que permita al usuario buscar información sobre ciudades.
# Tendrás un diccionario llamado ciudades_info que contiene
# información sobre algunas ciudades, como su país, población y puntos de interés.
# El programa debe permitir al usuario ingresar el nombre de una ciudad y mostrar la información correspondiente.
# El programa debe poder manejar el caso en el que la ciudad no existe en el diccionario
# y mostrando un mensaje avisando del error.

ciudades_info = {
    'Paris': {
        'Pais': 'Francia',
        'Poblacion': 2187526,
        'Puntos_de_Interes': ['Torre Eiffel', 'Louvre', 'Catedral de Notre-Dame']
    },
    'Nueva York': {
        'Pais': 'Estados Unidos',
        'Poblacion': 8398748,
        'Puntos_de_Interes': ['Estatua de la Libertad', 'Central Park', 'Times Square']
    },
    'Tokio': {
        'Pais': 'Japón',
        'Poblacion': 13929286,
        'Puntos_de_Interes': ['Torre de Tokio', 'Templo Senso-ji', 'Palacio Imperial']
    }
}
try:
    bus = input('Ingrese una ciudad: ').title()
    
    for llave, valor in ciudades_info.items():
        if llave == bus:
            print(
f'''Ciudad: {llave}
Pais: {valor['Pais']}
Poblacion: {valor['Poblacion']}
Puntos de interes: {valor['Puntos_de_Interes']}
'''
)
            break
except Exception as e:
    print(f'Ha ocurrido el siguiente error: {type(e).__name__}. Debido a que la ciudad {bus} no existe en la base de datos')
