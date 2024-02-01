# 5) Desarrollar una funcion que permita convertir un numero romano en un numero decimal.

decimal = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def numero_romano(num, pos, decimal):
    if (pos == (len(num)-1)):
        return decimal[num[pos]]
    else:
        letra_actual = decimal[num[pos]]
        letra_siguiente = decimal[num[pos+1]]
        if (letra_actual < letra_siguiente):
            return - letra_actual + numero_romano(num, pos+1, decimal)
        else:
            if (letra_actual >= letra_siguiente):
                return letra_actual + numero_romano(num, pos+1, decimal)

# print(numero_romano("XXIIIV", 0, decimal))

# -------------------------------------------------------------------------------------------

# Ejercicio 22:
# El problema de la mochila Jedi. Suponga que un Jedi
# (Luke Skywalker, Obi-Wan Kenobi, Rey u otro, el que más le guste)
# está atrapado, pero muy cerca está su mochila que contiene muchos objetos.
# Implementar una función recursiva llamada “usar la fuerza” que le permita al
# Jedi “con ayuda de la fuerza” realizar las siguientes actividades:

# A. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz
# o que no queden más objetos en la mochila;

# B. determinar si la mochila contiene un sable de luz y cuantos objetos fueron
# necesarios sacar para encontrarlo;

# C. Utilizar un vector para representar la mochila.


mochila = ["lapiz", "sable de luz", "casa"]


def UsarLaFuerza(mochila, pos):
    if (pos < len(mochila)):
        if (mochila[pos] == "sable de luz"):
            print("sable de luz se encuentra en la posicion: ", pos)
        else:
            return UsarLaFuerza(mochila, pos+1)
    else:
        print("sable de luz no se encutra en la mochila")

# print(UsarLaFuerza(mochila, 0))

# -------------------------------------------------------------------------------------------

# 23) Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido
#     en una matriz [nxn], solo se puede mover de a una casilla a la vez,
#     no se puede mover en diagonal y que la misma sea adyacente y no este marcada como pared
#     se comenzara en la casilla (0,0) y se termina en la (n-i, n-i), se mueve a la
#     siguiente casilla si es posible, cuando no se pueda avanzar hay que retroceder
#     sobre los pasos dados en busca de una camino alternativo.


lab = [
       [1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 0, 1],
       [1, 1, 1, 0, 1, 0, 1],
       [1, 0, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, 1, 2]
       ]


def SalidaLaberinto(matriz, x, y, caminos=[]):
    if (x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
        if (matriz[x][y] == 2):
            caminos.append([x, y])
            print("Saliste del laberinto")
            print(caminos)
            caminos.pop()
        elif (matriz[x][y] == 1):
            matriz[x][y] = 3
            caminos.append([x, y])
            SalidaLaberinto(matriz, x, y + 1, caminos)
            SalidaLaberinto(matriz, x, y - 1, caminos)
            SalidaLaberinto(matriz, x - 1, y, caminos)
            SalidaLaberinto(matriz, x + 1, y, caminos)
            caminos.pop()
            matriz[x][y] = 1


print(SalidaLaberinto(lab, 0, 0))
