from cola import Cola
from random import randint

# Ejercicio 18:
# Dada una cola con los códigos de turnos de atención (con el formato #@@@,
# donde # es una letra de la A hasta la F y “@@@” son tres dígitos desde el 000
# al 999), desarrollar un algoritmo que resuelva las siguientes situaciones:
# a. cargar 1000 turnos de manera aleatoria a la cola.
# b. separar la cola con datos en dos colas, cola_1 con losturnos que empiezan
# con la letra A, C y F, y la cola_2 conel resto de los turnos (B, D y E).
# c. determinar cuál de las colas tiene mayor cantidad de turnos,
# y de esta cuál de las letras tiene mayor cantidad.
# d. mostrar los turnos de la cola con menor cantidad de elementos, cuyo número
# de turno sea mayor que 506

'''

cola_1 = Cola()
cola_acf = Cola()
cola_bde = Cola()
cola_acf_aux = Cola()
cola_bde_aux = Cola()

cont_tur1 = 0
cont_tur2 = 0

A = 0
B = 0
C = 0
D = 0
E = 0
F = 0

print('Cola original')
# Punto A
for i in range(10):
    dato = (chr(randint(65, 70)), randint(000, 999))
    cola_1.arrive(dato)
    print(dato)

# Punto B

while cola_1.size() > 0:
    dato = cola_1.atention()
    if (dato[0] == 'A' or dato[0] == 'C' or dato[0] == 'F'):
        cola_acf.arrive(dato)
    else:
        cola_bde.arrive(dato)

# Punto C

print('Cola ACF')
while cola_acf.size() > 0:
    dato = cola_acf.atention()
    print(dato)
    cont_tur1 += 1
    if dato[1] > 506:
        cola_acf_aux.arrive(dato)
    if dato[0] == 'A':
        A += 1
    elif dato[0] == 'C':
        C += 1
    else:
        F += 1


print('Cola BDE')
while cola_bde.size() > 0:
    dato = cola_bde.atention()
    print(dato)
    cont_tur2 += 1
    if dato[1] > 506:
        cola_bde_aux.arrive(dato)
    if dato[0] == 'B':
        B += 1
    elif dato[0] == 'D':
        D += 1
    else:
        E += 1


if (cont_tur1 > cont_tur2):
    if (A > C and A > F):
        print('A es la letra con mas turnos')
    elif (C > A and C > F):
        print('C es la letra con mas turnos')
    elif (F > A and F > C):
        print('F es la letra con mas turnos')
    else:
        print('Todas la letra tienen la misma cantidad deturnos')
    print('La cola con mayoria de turno es la numero 1 con:', cont_tur1)
elif (cont_tur1 < cont_tur2):
    if (B > D and B > E):
        print('B es la letra con mas turnos')
    elif (D > B and D > E):
        print('D es la letra con mas turnos')
    elif (E > B and F > D):
        print('E es la letra con mas turnos')
    else:
        print('Todas la letra tienen la misma cantidad deturnos')
    print('La cola con mayoria de turno es la numero 2 con:', cont_tur2)
else:
    print('Las 2 colas tienen la misma cantidad.')

print(cola_acf_aux.size())
print(cola_bde_aux.size())

if (cola_acf_aux.size() < cola_bde_aux.size()):
    print('La cola con menor cantidad de tunos mayor de 506 es la 1')
    while cola_acf_aux.size() > 0:
        dato = cola_acf_aux.atention()
        print(dato)
else:
    print('La cola con menor cantidad de tunos mayor de 506 es la 2')
    while cola_bde_aux.size() > 0:
        dato = cola_bde_aux.atention()
        print(dato)

'''
# -------------------------------------------------------------------------------------------

# Ejercicio 22:
# Se tienen una cola con personajes de Marvel Cinematic Universe (MCU),
# de los cuales se conoce el nombre del personaje, el nombre del superhéroe y
# su género(Masculino M y Femenino F) –por ejemplo {Tony Stark, Iron Man, M},
# {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc.,
# desarrollar un algoritmo que resuelva las siguientes actividades:
# A.Determinar el nombre del personaje de la superhéroe Capitana Marvel;
# B.Mostrar los nombre de los superhéroes femeninos;
# C.Mostrar los nombres de los personajes masculinos;
# D.Determinar el nombre del superhéroe del personaje Scott Lang;
# E.Mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
#    con la letra S;
# F.Determinar si el personaje Carol Danvers se encuentra en la cola e
# indicar su nombrede superhéroes.


class Personajess ():

    def __init__(self, nomPersonaje, nomHeroe, genero):
        self.nomPersonaje = nomPersonaje
        self.nomHeroe = nomHeroe
        self.genero = genero

    def __str__(self):
        return f'{self.__nomPersonaje} - {self.__nomHeroe} - {self.__genero}'


personajes = [
    Personajess('Tony Stark', 'Iron Man', 'M'),
    Personajess('Steve Rogers', 'Capitán América', 'M'),
    Personajess('Natasha Romanoff', 'Black Widow', 'F'),
    Personajess('Carol Danvers', 'Capitana Marvel', 'F'),
    Personajess('Scott Lang', 'AntMan', 'M')
]

cola1 = Cola()
colaFemeninos = Cola()
colaMasculinos = Cola()
colaAux = Cola()

for personaje in personajes:
    cola1.arrive(personaje)

while cola1.size() > 0:
    value = cola1.atention()
    colaAux.arrive(value)
    if value.genero == 'F':
        colaFemeninos.arrive(value)
    else:
        colaMasculinos.arrive(value)
    if value.nomHeroe == 'Capitana Marvel':
        print('El nombre de la Capitana Marvel es:', value.nomPersonaje)
        print()
    if value.nomPersonaje == 'Scott Lang':
        print('El nombre de Heroe de Scott es:', value.nomHeroe)
    if value.nomPersonaje == 'Carol Danvers':
        print('Carol se encuentra en la cola y es:', value.nomHeroe)
        print()

print()
print('Datos de personajes con S:')
while colaAux.size() > 0:
    value = colaAux.atention()
    if (value.nomHeroe[0] == 'S' or value.nomPersonaje[0] == 'S'):
        print(value.nomHeroe, value.nomPersonaje, value.genero)

print()
print('Lista de superheroes femeninos:')
while colaFemeninos.size() > 0:
    value = colaFemeninos.atention()
    print(value.nomHeroe)

print()
print('Lista de nombres maculinos:')
while colaMasculinos.size() > 0:
    value = colaMasculinos.atention()
    print(value.nomPersonaje)
