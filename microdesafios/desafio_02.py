ganadores = {
    '1990': 'Alemania',
    '1994': 'Brasil',
    '1998': 'Francia',
    '2002': 'Brasil',
    '2006': 'Italia',
    '2010': 'España',
    '2014': 'Alemania',
    '2018': 'Francia',
}
key = int(input("Ingrese el año del mundial: "))
value = input(f"Ingrese al ganador del mundial {key}: ")

ganadores[key] = value

print(ganadores)
