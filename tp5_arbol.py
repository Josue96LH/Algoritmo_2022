from arbol_binario import BinaryTree

# EJERCICIO 5:
# Dado un árbol con los nombre de los superhéroes y villanos de la
# saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que contemple
# lo siguiente:
# A. además del nombre del superhéroe, en cada nodo del árbol se almacenará un
# campo booleano que indica si es un héroe o un villano,
# True y False respectivamente;
# B. listar los villanos ordenados alfabéticamente;
# C. mostrar todos los superhéroes que empiezan con C;
# D. determinar cuántos superhéroes hay el árbol;
# E. Doctor Strange en realidad está mal cargado.Utilice una búsqueda por
# proximidad para encontrarlo en el árbol y modificar su nombre;
# F. listar los superhéroes ordenados de manera descendente;
# G. generar un bosque a partir de este árbol, un árbol debe contener a
# los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol

'''

arbol = BinaryTree()
heroes = BinaryTree()
villanos = BinaryTree()


datos = [
    {'name': 'iron man', 'is_hero': True},
    {'name': 'capitana marvel', 'is_hero': True},
    {'name': 'thor', 'is_hero': True},
    {'name': 'doc strange', 'is_hero': True},
    {'name': 'thanos', 'is_hero': False},
    {'name': 'red skull', 'is_hero': False},
    {'name': 'capitan america', 'is_hero': True}
]

for personajes in datos:
    arbol.insert_node(personajes['name'], personajes['is_hero'])

# A
arbol.inorden()
print()

# B
arbol.inorden_super_or_villano()

print()
# C
arbol.search_by_coincidence('c')

print()
# D
print(f'En el arbol hay {arbol.contar_heroes()} heroes.')

print()
# E
print('Se modifica doc strange x doctor strange')
pos = arbol.search('doc strange')
if pos is not None:
    pos.value = 'doctor strange'

arbol.search_by_coincidence('doctor strange')

print()
# F
print('Listado descendente heroes: ')
arbol.postorden_super_or_villano()

print()
# G
arbol.by_level()

'''
# ------------------------------------------------------------------------------------------

arbol = BinaryTree()

datos = [
    {'name': 'Ceto', 'derrotado': None},               {'name': 'Tifón', 'derrotado': 'Zeus'},                {'name': 'Equidna', 'derrotado': 'Argos Panoptes'},
    {'name': 'Dino', 'derrotado': None},               {'name': 'Pefredo', 'derrotado': None},                {'name': 'Enio', 'derrotado': None},
    {'name': 'Escila', 'derrotado': None},             {'name': 'Caribdis', 'derrotado': None},               {'name': 'Euríale', 'derrotado': None},
    {'name': 'Esteno', 'derrotado': None},             {'name': 'Medusa', 'derrotado': 'Perseo'},             {'name': 'Ladón', 'derrotado': 'Heracles'},
    {'name': 'Aguila del Cáucaso', 'derrotado': None}, {'name': 'Quimera', 'derrotado': 'Belerofonte'},       {'name': 'Hidra de Lerna', 'derrotado': 'Heracles'},
    {'name': 'León de Nemea', 'derrotado': 'Heracles'}, {'name': 'Esfinge', 'derrotado': 'Edipo'},            {'name': 'Dragón de la Cólquida', 'derrotado': None},
    {'name': 'Cerbero', 'derrotado': None},            {'name': 'Cerda de Cromión', 'derrotado': 'Teseo'},    {'name': 'Ortro', 'derrotado': 'Heracles'},
    {'name': 'Toro de Creta', 'derrotado': 'Teseo'},   {'name': 'Jabalí de Calidón', 'derrotado': 'Atalanta'},{'name': 'Carcinos', 'derrotado': None},
    {'name': 'Gerión', 'derrotado': 'Heracles'},       {'name': 'Cloto', 'derrotado': None},                  {'name': 'Láquesis', 'derrotado': None},
    {'name': 'Atropos', 'derrotado': None},            {'name': 'Minotauro de Creta', 'derrotado': 'Teseo'},  {'name': 'Harpías', 'derrotado': None},
    {'name': 'Argos Panoptes', 'derrotado': 'Hermes'}, {'name': 'Aves del Estínfalo', 'derrotado': None},     {'name': 'Talos', 'derrotado': 'Medea'},
    {'name': 'Sirenas', 'derrotado': None},            {'name': 'Pitón', 'derrotado': 'Apolo'},               {'name': 'Cierva de Cerinea', 'derrotado': None},
    {'name': 'Basilisco', 'derrotado': None},          {'name': 'Jabalí de Erimanto', 'derrotado': None},
]

for criatura in datos:
    arbol.insert_node(criatura['name'], {'derrotado': criatura['derrotado']})

# A
print('Listado de criaturas y quien los derroto')
arbol.inorden_criaturas()

# B
arbol.inorden_add_descripcio()

# C
pos = arbol.search('Talos')
if pos is not None:
    print('Informacion sobre Talos:', pos.value, 'derrotado por', pos.other_values['derrotado'])

# D
print('Lista de los 3 dioses que mas criaturas derrotaron:')
dic_ranking = {}
arbol.inorden_ranking(dic_ranking)

# print(dic_ranking)


def order_por(item):
    # print(item)
    return item[1]


ordenados = list(dic_ranking.items())
ordenados.sort(key=order_por, reverse=True)
print(ordenados[:3])

# E
print()
print('Criaturas derrotadas por Heracles.')
arbol.inorden_derrotatos_heracles()

# F
print()
print('Criaturas no derrotas.')
arbol.inorden_no_derrotatos()

# G
print()
arbol.inorden_add_field()

# H
pos = arbol.search('Cerbero')
if pos is not None:
    pos.other_values['capturado'] = 'Heracles'
pos = arbol.search('Toro de Creta')
if pos is not None:
    pos.other_values['capturado'] = 'Heracles'
pos = arbol.search('Cierva de Cerinea')
if pos is not None:
    pos.other_values['capturado'] = 'Heracles'
pos = arbol.search('Jabalí de Erimanto')
if pos is not None:
    pos.other_values['capturado'] = 'Heracles'

# J

arbol.delete_node('Basilisco')
arbol.delete_node('Sirenas')

# K
pos = arbol.search('Aves del Estínfalo')
if pos is not None:
    pos.other_values['descripcio'] = 'Heracles derroto a varias'

# L
pos = arbol.search('Ladón')
if pos is not None:
    pos.value = 'Dragón Ladón'

arbol.search_by_coincidence('Dragón Ladón')

# M
print('Listado por nivel: ')
arbol.by_level()

# N
print()
print('Lista capturados por Heracles: ')
arbol.inorden_capturados_heracles()

print()
arbol.preorden()
print()
