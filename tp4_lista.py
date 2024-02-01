from lista_lista import Lista
from random import randint
from lista import Lista

# Ejercicio 15:
# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce:
# nombre, cantidad de torneos ganados, cantidad de batallas perdidas y
# cantidad de batallas ganadas. Y además la lista de sus Pokémons, de los cuales se sabe:
# nombre, nivel, tipo y subtipo. Se pide resolver las siguientes actividades
# utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons:
# Tyrantrum, Terrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;

'''

class Entrenador():

    def __init__(self, nombre, torGanados=0, battGanadas=0, battPerdidas=0):
        self.nombre = nombre
        self.torGanados = torGanados
        self.battGanadas = battGanadas
        self.battPerdidas = battPerdidas

    def __str__(self):
        return f'{self.nombre} = TG:{self.torGanados} - BG:{self.battGanadas} - BP:{self.battPerdidas}'


class Pokemon():

    def __init__(self, nombre, tipo, nivel=1, subtipo=None):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f'{self.nombre} - {self.nivel} - {self.tipo} - {self.subtipo}'


entrenadores = [
    Entrenador('Ash', torGanados=randint(1, 10), battGanadas=randint(1, 10), battPerdidas=randint(1, 10)),
    Entrenador('Red', torGanados=randint(1, 10), battGanadas=randint(1, 10), battPerdidas=randint(1, 10)),
    Entrenador('Blue', torGanados=randint(1, 10), battGanadas=randint(1, 10), battPerdidas=randint(1, 10)),
    Entrenador('Gary', torGanados=randint(1, 10), battGanadas=randint(1, 10), battPerdidas=randint(1, 10)),
    Entrenador('Brook', torGanados=randint(1, 10), battGanadas=randint(1, 10), battPerdidas=randint(1, 10)),
    Entrenador('Misty',  torGanados=randint(1, 10), battGanadas=randint(1, 10), battPerdidas=randint(1, 10)),
]

lista_entrenadores = Lista()

pokemons = [
    Pokemon('pikachu', 'electrico', randint(1, 20)),
    Pokemon('jolteon', 'electrico', randint(1, 20)),
    Pokemon('vaporeon', 'agua', randint(1, 20)),
    Pokemon('flareon', 'fuego', randint(1, 20)),
    Pokemon('leafeon', 'planta', randint(1, 20)),
    Pokemon('Terrakion', 'tierra', randint(1, 20)),
]

for entrenador in entrenadores:
    lista_entrenadores.insert(entrenador, 'nombre')

for pokemon in pokemons:
    numero_entrenador = randint(0, lista_entrenadores.size()-1)
    entrenador = lista_entrenadores.get_element_by_index(numero_entrenador)
    entrenador[1].insert(pokemon, 'nombre')

lista_entrenadores.barrido_entrenadores()
print()

# A
entrenador = input('Ingrese el nombre del entrenador: ')
pos = lista_entrenadores.search(entrenador, 'nombre')
if (pos):
    value = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = value[0], value[1]
    print(f'{entrenador.nombre} tiene {sublista.size()} pokemons')
else:
    print('No se encuentra ese entrenador.')

print()
# B
print('Entrenadores con 4 torneos ganados o mas: ')
lista_entrenadores.barrido_cantidad_torneos_ganados(3)

print()
# C
mayor_cantidad = lista_entrenadores.get_element_by_index(0)[0].torGanados
pos_mayor = 0

for pos in range(1, lista_entrenadores.size()):
    entrenador = lista_entrenadores.get_element_by_index(pos)[0]
    if entrenador.torGanados > mayor_cantidad:
        pos_mayor = pos
        mayor_cantidad = entrenador.torGanados

value = lista_entrenadores.get_element_by_index(pos_mayor)
entrenador, sublista = value[0], value[1]

if sublista.size() > 0:
    pokemon_mayor = sublista.get_element_by_index(0)
    for pos in range(1, sublista.size()):
        pokemon = sublista.get_element_by_index(pos)
        if pokemon.nivel > pokemon_mayor.nivel:
            pokemon_mayor = pokemon
    print(f'El pokemon de mayor nivel de {entrenador.nombre} es {pokemon_mayor.nombre} de nivel {pokemon_mayor.nivel}')

print()
# D

entrenador = input('Ingrese el nombre del entrenador: ')
pos = lista_entrenadores.search(entrenador, 'nombre')
if (pos):
    value = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = value[0], value[1]
    print(value[0])
    print('Pokemons ----------------')
    sublista.barrido()
else:
    print('No se encuentra ese entrenador.')

print()
# E

print('Entrenador con 79% de victoria: ')
lista_entrenadores.barrido_porcentaje_victorias()
print()

# F
print('Entrenadores fuego')
for pos in range(0, lista_entrenadores.size()):
    value = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = value[0], value[1]
    if sublista.size() > 0:
        for pos in range(0, sublista.size()):
            pokemon = sublista.get_element_by_index(pos)
            if ('fuego' == pokemon.tipo or 'planta' == pokemon.tipo):
                print(f'El {entrenador.nombre} tiene pokemones de tipo fuego o planta')
            elif ('agua' == pokemon.tipo and 'volador' == pokemon.subtipo):
                print(f'El {entrenador.nombre} tiene pokemones de tipo agua y subtipo volador')
print()

# G

entrenador = input('Ingrese el nombre del entrenador: ')
pos = lista_entrenadores.search(entrenador, 'nombre')
if pos is not None:
    valor = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = valor[0], valor[1]

if sublista.size() > 0:
    total = 0
    promedio_nivel = 0
    for pos in range(0, sublista.size()):
        pokemon = sublista.get_element_by_index(pos)
        total = pokemon.nivel + total
    promedio_nivel = total / sublista.size()
    print(f'El entrenador {entrenador.nombre} tiene un promedio de {promedio_nivel} niveles por pokemon')
else:
    print('No tiene pokemons')

print()

# H
buscado = input('Ingrese el nombre del pokemon: ')
contPok = 0
for pos in range(0, lista_entrenadores.size()):
    value = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = value[0], value[1]
    if sublista.size() > 0:
        for pos in range(0, sublista.size()):
            pokemon = sublista.get_element_by_index(pos)
            if pokemon.nombre == buscado:
                contPok += 1
if contPok > 0:
    print(f'{contPok} entrenadores tiene a {buscado}')
else:
    print('Pokemon no encontrado')

print()
# I
print('Entrenadores con pokemons repetidos: ')
for pos in range(0, lista_entrenadores.size()):
    cont_poke_repe = 0
    aux = ''
    value = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = value[0], value[1]
    if sublista.size() > 0:
        for pos in range(0, sublista.size()):
            pokemon = sublista.get_element_by_index(pos)
            if pokemon.nombre == aux:
                cont_poke_repe += 1
            aux = pokemon.nombre
if cont_poke_repe != 0:
    print(f'El entrenador{entrenador.nombre} tiene {cont_poke_repe} pokemons repetidos')
else:
    print('Los entrenadores no tienen pokemones repetidos')

print()
# J
print('Entrenadores con ciertos pokemons: ')
for pos in range(0, lista_entrenadores.size()):
    value = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = value[0], value[1]
    if sublista.size() > 0:
        for pos in range(0, sublista.size()):
            pokemon = sublista.get_element_by_index(pos)
            if pokemon.nombre == 'Tyrantrum' or pokemon.nombre == 'Terrakion' or pokemon.nombre == 'Wingull':
                print(f'El entrenador {entrenador.nombre}, tiene un Tyrantrum, Terrakion o Wingull')

print()
# K
print('Buqueda Entrenador y Pokemon: ')
entrenador = input('Ingrese el nombre del entrenador: ')
pos = lista_entrenadores.search(entrenador, 'nombre')
if pos is not None:
    valor = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = valor[0], valor[1]

buscado = input('Ingrese el nombre del Pokemon: ')
if sublista.size() > 0:
    for pos in range(0, sublista.size()):
        pokemon = sublista.get_element_by_index(pos)
        if buscado == pokemon.nombre:
            print(entrenador)
            print(pokemon)

'''
# ---------------------------------------------------------------------------------------------

# Ejercicio 21:
# Se cuenta con una lista de películas de cada una de estas se dispone de los 
# siguientes datos:
# nombre, valoración del público –es un valor comprendido entre 0-10–, 
# año de estreno y recaudación. Desarrolle los algoritmos necesarios para realizar 
# las siguientes tareas:
# A) permitir filtrar las películas por año –es decir mostrar todas las películas de un 
# determinado año–;
# B). mostrar los datos de la película que más recaudo;
# C) indicar las películas con mayor valoración del público, puede ser más de una;
# D). mostrar el contenido de la lista en los siguientes criterios de orden
# –solo podrá utilizar una lista auxiliar–:
# I. por nombre,
# II. por recaudación,
# III. por año de estreno,
# IV. por valoración del público.

'''

class Pelicula:

    def __init__(self, nombre, anio, valorPub, recaudacion):
        self.nombre = nombre
        self.anio = anio
        self.valorPub = valorPub
        self.recaudacion = recaudacion

    def __str__(self):
        return f'{self.nombre} = Anio: {self.anio} - Stars: {self.valorPub} - ${self.recaudacion}'


lista_peliculas = Lista()
lista_aux = Lista()

peliculas = [
    {'film': 'La red social', 'year': '2010', 'star': 10, 'many': '100.00'},
    {'film': 'Toy Story 3', 'year': '2010', 'star': 7, 'many': '2000.00'},
    {'film': 'Skyfall', 'year': '2012', 'star': 7, 'many': '11851.00'},
    {'film': 'Origen', 'year': '2010', 'star': 6, 'many': '500.00'},
    {'film': 'El Gran Hotel Budapest', 'year': '2014', 'star': 6, 'many': '4044.00'},
    {'film': 'El topo', 'year': '2011', 'star': 5, 'many': '2500.00'},
    {'film': 'Wonder', 'year': '2017', 'star': 7, 'many': '87817.00'},
    {'film': 'La invención de Hugo', 'year': '2011', 'star': 1, 'many': '1700.00'},
    {'film': 'Coco', 'year': '2017', 'star': 10, 'many': '34044.00'},
    {'film': 'Gravity',  'year': '2013', 'star': 4, 'many': ' 15454.00'},
    {'film': 'Marvel Los Vengadores', 'year': '2012', 'star': 8, 'many': '300000.00'},
    {'film': 'Blue Jasmine', 'year': '2013', 'star': 3, 'many': '5440.00'},
    {'film': 'Descifrando Enigma', 'year': '2014', 'star': 9, 'many': '14464.00'},
    {'film': 'Sicario', 'year': '2015', 'star': 4, 'many': '5145.00'},
    {'film': '12 años de esclavitud', 'year': '2013', 'star': 5, 'many': '5814.00'},
    {'film': 'Bohemian Rhapsody', 'year': '2018', 'star': 9, 'many': '84554.00'},
]

for peli in peliculas:
    lista_peliculas.insert(Pelicula(peli['film'],
                                    peli['year'],
                                    peli['star'],
                                    peli['many']), 'nombre')

lista_peliculas.barrido()

print()
# A
anio_buscado = input('Ingrese el anio que desea buscar: ')
lista_peliculas.barrido_anio_buscado(anio_buscado)

print()
# B
mayor_recaudacion = lista_peliculas.get_element_by_index(0).recaudacion
pos_mayor = 0

for pos in range(0, lista_peliculas.size()):
    pelicula = lista_peliculas.get_element_by_index(pos)
    if pelicula.recaudacion > mayor_recaudacion:
        pos_mayor = pos
        mayor_recaudacion = pelicula.recaudacion
value = lista_peliculas.get_element_by_index(pos_mayor)
print('Pelicula con mayor recaudacion: ')
print(f'{value.nombre} con ${mayor_recaudacion}')

print()
# C
print('Peliculas con mayor valoracion: ')
mayor_valorPub = lista_peliculas.get_element_by_index(0).valorPub

for pos in range(1, lista_peliculas.size()):
    pelicula = lista_peliculas.get_element_by_index(pos)
    if pelicula.valorPub > mayor_valorPub:
        mayor_valorPub = pelicula.valorPub

for pos in range(0, lista_peliculas.size()):
    pelicula = lista_peliculas.get_element_by_index(pos)
    if pelicula.valorPub == mayor_valorPub:
        print(f'{pelicula.nombre} con {pelicula.valorPub} estrellas')

print()
# D
print('Elija la opcion: ')
opcion = input('(1) por nombre, (2) por año de estreno, (3) por valoración del público, (4) por recaudación. ')
print()

if opcion == '1':
    orden = 'nombre'
elif opcion == '2':
    orden = 'anio'
elif opcion == '3':
    orden = 'valorPub'
elif opcion == '4':
    orden = 'recaudacion'
else:
    orden = ' '
    print('Ingreso una opcion incorrecta.')


if (orden != ' '):
    for peli in peliculas:
        lista_aux.insert(Pelicula(peli['film'],
                                  peli['year'],
                                  peli['star'],
                                  peli['many']), orden)

lista_aux.barrido()

'''
# ------------------------------------------------------------------------------------------


class Jedi:

    # Ejercicio 22:

    # Se dispone de una lista de todos los Jedi, de cada uno de estos se
    # conoce su nombre, maestros, colores de sable de luz usados y especie.
    # implementar las funciones necesarias
    # para resolver las actividades enumeradas a continuación:
    # a. listado ordenado por nombre y por especie;
    # b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
    # c. mostrar todos los padawan de Yoda y Luke Skywalker, aprendices;
    # d. mostrar los Jedi de especie humana y twi'lek;
    # e. listar todos los Jedi que comienzan con A;
    # f. mostrar los Jedi que usaron sable de luz de más de un color;
    # g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
    # h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu,
    # si los tuvieron.

    def __init__(self, nombre, especie, nombMaestro, colorSables):
        self.nombre = nombre
        self.especie = especie
        self.nombMaestro = nombMaestro
        self.colorSables = colorSables

    def __str__(self):
        return f"{self.nombre} | {self.especie} | {self.nombMaestro} | {self.colorSables}"


lista_jedi = Lista()
lista_especie = Lista()

file = open('jedis.txt')
lineas = file.readlines()

lista = []

lineas.pop(0)  # quitar cabecera
for linea in lineas:
    datos = linea.split(';')  # separa el texto cuando encuentra ;
    datos.pop(-1)  # elimina el ultimo elemento

    lista_jedi.insert(Jedi(datos[0],
                           datos[2],
                           datos[3].split('/'),
                           datos[4].split('/')),
                      criterio='nombre')
    lista_especie.insert(Jedi(datos[0],
                              datos[2],
                              datos[3],
                              datos[4].split('/')),
                         criterio='especie')
    lista.append(Jedi(datos[0],
                      datos[2],
                      datos[3].split('/'),
                      datos[4].split('/')))

# A
lista_jedi.barrido()
print('--------------------------------------------')
lista_especie.barrido()

print()
# B
lista_jedi.barrido_pjBus()

print()
# C
lista_especie.barrido_aprendices()

print()
# D
lista_especie.barrido_hum_twi()

print()
# E
lista_jedi.barrido_jedis_a()

print()
# F
lista_jedi.barrido_sables()

print()
# G
lista_jedi.barrido_sables_aov()

print()
# H
lista_jedi.barrido_aprendices_2()

print()
