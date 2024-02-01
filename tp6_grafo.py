from grafo import Grafo

# Ejercicio 14:
# Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:
# A. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# B. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la 
# distancia entre los ambientes, se debe cargar en metros;
# C. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
# D. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.


# punto A: cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
'''
mi_grafo = Grafo(dirigido=False)

# 1
mi_grafo.insertar_vertice('cocina')
# 2
mi_grafo.insertar_vertice('comedor')
# 3
mi_grafo.insertar_vertice('cochera')
# 4
mi_grafo.insertar_vertice('quincho')
# 5
mi_grafo.insertar_vertice('baño 1')
# 6
mi_grafo.insertar_vertice('baño 2')
# 7
mi_grafo.insertar_vertice('habitación 1')
# 8
mi_grafo.insertar_vertice('habitación 2')
# 9
mi_grafo.insertar_vertice('sala de estar')
# 10
mi_grafo.insertar_vertice('terraza')
# 11
mi_grafo.insertar_vertice('patio')


# punto B: cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la 
# distancia entre los ambientes, se debe cargar en metros;

mi_grafo.insertar_arista('cocina', 'comedor', 1)
mi_grafo.insertar_arista('cocina', 'baño 2', 5)
mi_grafo.insertar_arista('cocina', 'habitación 1', 6)
mi_grafo.insertar_arista('comedor', 'cochera', 1)
mi_grafo.insertar_arista('comedor', 'quincho', 2)
mi_grafo.insertar_arista('cochera', 'habitación 1', 4)
mi_grafo.insertar_arista('cochera', 'habitación 2', 5)
mi_grafo.insertar_arista('quincho', 'baño 1', 1)
mi_grafo.insertar_arista('quincho', 'habitación 2', 4)
mi_grafo.insertar_arista('baño 1', 'habitación 2', 3)
mi_grafo.insertar_arista('baño 1', 'sala de estar', 4)
mi_grafo.insertar_arista('baño 2', 'habitación 1', 1)
mi_grafo.insertar_arista('baño 2', 'terraza', 4)
mi_grafo.insertar_arista('habitación 1', 'terraza', 3)
mi_grafo.insertar_arista('habitación 1', 'patio', 4)
mi_grafo.insertar_arista('habitación 2', 'terraza', 2)
mi_grafo.insertar_arista('habitación 2', 'sala de estar', 1)
mi_grafo.insertar_arista('sala de estar', 'patio', 2)
mi_grafo.insertar_arista('terraza', 'patio', 1)

# Punto C: obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;

arbol_min = mi_grafo.kruskal_minimo()

arbol_min = arbol_min[0].split('-')
peso_total = 0
for nodo in arbol_min:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
    print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')
print(f"el peso total es {peso_total}")


# Punto D: determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.

print('\nEl camino más corto')
resultados = mi_grafo.dijkstra('habitación 1')
camino = mi_grafo.camino(resultados, 'habitación 1', 'sala de estar')
print(camino)

print()
'''

# --------------------------------------------------------------------------------------------

# Ejercicio 15:
# Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas y naturales 
# del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
# A. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
#uno en las naturales) y tipo (natural o arquitectónica);
# B. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;
# C. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
# D. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
# E. determinar si algún país tiene más de una maravilla del mismo tipo;
# F. deberá utilizar un grafo no dirigido.

mi_grafo = Grafo(dirigido=False)

# maravillasnaturales
mi_grafo.insertar_vertice('T', datos={'tipo': 'Nat', 'pais': 'egipto'})
mi_grafo.insertar_vertice('Z', datos={'tipo': 'Nat', 'pais': 'francia'})
mi_grafo.insertar_vertice('F', datos={'tipo': 'Nat', 'pais': 'china'})
mi_grafo.insertar_vertice('X', datos={'tipo': 'Nat', 'pais': 'india'})
mi_grafo.insertar_vertice('R', datos={'tipo': 'Nat', 'pais': 'eeuu'})
mi_grafo.insertar_vertice('K', datos={'tipo': 'Nat', 'pais': 'brasil'})

# maravillas arquitectonicas
mi_grafo.insertar_vertice('L', datos={'tipo': 'Arq', 'pais': 'argentina-brasil-paragauy'})
mi_grafo.insertar_vertice('J', datos={'tipo': 'Arq', 'pais': 'indonesia'})
mi_grafo.insertar_vertice('I', datos={'tipo': 'Arq', 'pais': 'sudafrica'})
mi_grafo.insertar_vertice('M', datos={'tipo': 'Arq', 'pais': 'india'})
mi_grafo.insertar_vertice('S', datos={'tipo': 'Arq', 'pais': 'china'})
mi_grafo.insertar_vertice('Y', datos={'tipo': 'Arq', 'pais': 'brasil'})

mi_grafo.insertar_arista('L', 'J', 6)
mi_grafo.insertar_arista('L', 'I', 3)
mi_grafo.insertar_arista('I', 'M', 8)
mi_grafo.insertar_arista('M', 'S', 2)
mi_grafo.insertar_arista('M', 'Y', 2)
mi_grafo.insertar_arista('Y', 'I', 9)

mi_grafo.insertar_arista('T', 'X', 6)
mi_grafo.insertar_arista('T', 'F', 3)
mi_grafo.insertar_arista('T', 'R', 8)
mi_grafo.insertar_arista('F', 'X', 2)
mi_grafo.insertar_arista('F', 'R', 2)
mi_grafo.insertar_arista('X', 'Z', 9)
mi_grafo.insertar_arista('R', 'Z', 4)
mi_grafo.insertar_arista('K', 'Z', 3)
mi_grafo.insertar_arista('R', 'X', 5)

print('Vertices:\n')

mi_grafo.barrido_vertice()


paises = mi_grafo.contar_maravillas()
for pais in paises:
    print(pais, paises[pais])


arbol_min = mi_grafo.kruskal_minimo()

arbol_min = arbol_min[0].split('-')
peso_total = 0
for nodo in arbol_min:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
    print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')

print(f"El peso total es {peso_total}")

# Punto c: hallar el árbol de expansión mínimo de cada tipo de las maravillas;
arbol = mi_grafo.kruskal_minimo()

for i in range(len(arbol)):
    arbol = mi_grafo.kruskal_minimo()
    arbol = arbol[i].split('-')
    peso_total = 0
    for nodo in arbol:
        nodo = nodo.split(';')
        peso_total += int(nodo[2])
        print(f'{nodo[0]} - {nodo[1]} - {nodo[2]} ')
    print(f"\nLa distancia total a recorrer: {peso_total} Km ")
    print()



# Punto d: determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
print('D. determinar si existen países que dispongan de maravillas arquitectónicas y naturales\n')
paises = mi_grafo.contar_maravillas()
tiene_maravillas = False
for pais in paises:
    if paises[pais]['Arq'] is True and paises[pais]['Nat'] is True:
        print(pais, 'Tiene de las 2 maravillas')
        tiene_maravillas = True

if tiene_maravillas is False:
    print(' No hay ')

# Punto e: determinar si algún país tiene más de una maravilla del mismo tipo;
print()
print('E. determinar si algún país tiene más de una maravilla del mismo tipo\n')
paises = mi_grafo.contar_maravillas_tipo()
tiene_maravillas = False
for pais in paises:
    if paises[pais]['Arq'] > 1:
        print(pais, 'Tiene mas de una Maravilla Arquitectonica')
        tiene_maravillas = True
    if paises[pais]['Nat'] > 1:
        print(pais, 'Tiene mas de una Maravilla Natural')
        tiene_maravillas = True

if tiene_maravillas is False:
    print('No hay paises con las maravillas del mismo tipo ')

print()
