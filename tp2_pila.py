from pila import Pila

# Ejercicio 19:
# Dada una pila de películas de las que se conoce su título, estudio
# cinematográfico y año de estreno, desarrollar las funciones
# necesarias para resolver las siguientes actividades:
# A.Mostrar los nombre películas estrenadas en el año 2014;
# B.Indicar cuántas películas se estrenaron en el año 2018;
# C.Mostrar las películas de Marvel Studios estrenadas en el año 2016.

'''
class Peliculas ():

    def __init__(self, titulo, estudio, year):
        self.__titulo = titulo
        self.__year = year
        self.__estudio = estudio

    def get_titulo(self):
        return self.__titulo

    def get_estudio(self):
        return self.__estudio

    def get_year(self):
        return self.__year

    def __str__(self):
        return f'{self.__titulo} - {self.__estudio} - {self.__year}'


pelis = [
    Peliculas('Iron Man', 'Marvel', 2008),
    Peliculas('The Avengers', 'Marvel', 2012),
    Peliculas('Spider-Man: No Way Home', 'Pixar', 2018),
    Peliculas('Capitan America: Civil War', 'Marvel', 2016),
    Peliculas('Doctor Strange', 'Marvel', 2016),
    Peliculas('Guardianes de la Galaxia', 'Marvel', 2014),
]

pila_1 = Pila()
pila_aux = Pila()
cont_pelis_2018 = 0


for peli in pelis:
    pila_1.push(peli)


while pila_1.size() > 0:
    dato = pila_1.pop()
    if dato.get_year() == 2014:
        print('En el 2014 se estrenaron: ', dato.get_titulo())

    if dato.get_year() == 2018:
        cont_pelis_2018 += 1

    if dato.get_estudio() == 'Marvel' and dato.get_year() == 2016:
        print('En 2016 el estudio marvel estreno: ', dato.get_titulo())


print('Cantidad de peliculas estrenadas en el 2018: ', cont_pelis_2018)

'''

# -------------------------------------------------------------------------------------------

# Ejercicio 24:
# Dada una pila de personajes de Marvel Cinematic Universe (MCU),
# de los cualesse dispone de su nombre y la cantidad de
# películas de la saga en la que participó, implementar
# las funciones necesarias para resolver las siguientes actividades:
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando
# como posición uno la cima de la pila;
# b. determinar los personajes que participaron en más de 5 películas de la saga,
# además indicar la cantidad de películas en la que aparece;
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G


class Peliculas ():

    def __init__(self, titulo, hero, cantidad):
        self.__titulo = titulo
        self.__hero = hero
        self.__cantidad = cantidad

    def get_titulo(self):
        return self.__titulo

    def get_hero(self):
        return self.__hero

    def get_cantidad(self):
        return self.__cantidad

    def __str__(self):
        return f'{self.__titulo} - {self.__hero} - {self.__cantidad}'


cont = 0
cont1 = 0
cont2 = 0

pelis = [
    Peliculas('Iron Man', 'Viuda Negra', 3),
    Peliculas('Iron Man I', 'Capitan america', 8),
    Peliculas('Guardian Galaxy', 'Groot', 7),
    Peliculas('Guardian Galaxy', 'Rocket Raccoon', 4),
    Peliculas('Capitan America', 'Diron man', 3)
]

pila_1 = Pila()
aux_pila = Pila()

for peli in pelis:
    pila_1.push(peli)


while pila_1.size() > 0:
    dato = pila_1.pop()
    cont += 1
    if dato.get_hero() == 'Rocket Raccoon':
        cont1 += cont
    if dato.get_hero() == 'Groot':
        cont2 += cont
    if dato.get_cantidad() >= 5:
        print('El personaje', dato.get_hero(), 'participo en', dato.get_cantidad(), 'peliculas')
    if dato.get_hero() == 'Viuda Negra':
        print('La Viuda Negra participo en:', dato.get_cantidad())
    nombre = dato.get_hero()
    if nombre[0] == 'C':
        print('Empieza con C:', nombre)
    if nombre[0] == 'D':
        print('Empieza con D:', nombre)
    if nombre[0] == 'G':
        print('Empieza con G:', nombre)
    aux_pila.push(dato)

print('Posicion de Rocket Raccon', cont1)
print('Posicion de Groot', cont2)
