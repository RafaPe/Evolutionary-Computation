import random
import copy

def make_graph(matrix):
    graph = {}
    for c in range(len(matrix)):
        i = c
        costo = {}
        for w in matrix[c]:
            ciudad = 'c' + str(i+1)
            costo[ciudad] = w
            i += 1
        ciudad = 'c' + str(c)
        graph[ciudad] = costo

    for i in range(1,len(matrix)):
        for j in range(i-1,-1,-1):
            a = 'c' + str(i)
            b = 'c' + str(j)
            graph[a][b] = graph[b][a]

    a = 'c' + str(len(matrix))
    graph[a] = {}
    for i in range(len(matrix)):
        b = 'c' + str(i)
        graph[a][b] = graph[b][a]

    return graph

''' Función para generar la solución inicial con algoritmo greedy'''
def generate_initial_sol(graph):
    initial_sol = ['c0']
    cost = 0
    ciudad_inicial = 'c0'
    
    while len(initial_sol) < 10:
        cuidad_menor_costo = ''
        menor = float('inf')
        for city in graph[ciudad_inicial]:
            if graph[ciudad_inicial][city] < menor and city not in initial_sol:
                menor = graph[ciudad_inicial][city]
                cuidad_menor_costo = city
        cost += menor
        ciudad_inicial = cuidad_menor_costo
        initial_sol.append(ciudad_inicial)
    
    cost += graph[initial_sol[-1]]['c0']

    return initial_sol, cost

'''Función para generar el vecindario'''
def generate_vecindario(graph, lista_tabu, s):
    #Actualizamos la lista tabú en caso de tener elementos
    eliminate = []
    for k in lista_tabu:
        if lista_tabu[k] == 0:
            eliminate.append(k)
    for e in eliminate:
        lista_tabu.pop(e)
    for k in lista_tabu:
        lista_tabu[k] = lista_tabu[k] - 1

    #Seleccionamos una cuidad "p" aleatoria para cambiarla de posición y generar el vecindario
    vecindario = []
    p = random.randint(1,len(s)-1)
    while s[p] in lista_tabu:  #Queremos una cuidad "p" aleatoria que no esté en la lista tabú
        p = random.randint(1,len(s)-1)
    if s[p] not in lista_tabu:
        for i in range(1,len(s)):
            if i == p:
                continue
            else:
                s2 = copy.deepcopy(s)
                a, b = s[i], s[p]
                s2[i], s2[p] = b, a
                vecindario.append(s2)
        lista_tabu[s[p]] = len(graph)//2 #Agregamos la cuidad "p" a la lista tabú 
    return vecindario, lista_tabu

'''Función para calcular el costo de un camino'''
def path_cost(camino, graph):
    cost = 0
    for i in range(len(camino)-2):
        a, b = camino[i], camino[i+1]
        cost += graph[a][b]
    cost += graph[camino[-1]]['c0']

    return cost

'''Función de búsqueda Tabú'''
def busqueda_tabu(graph, max_iter):
    lista_tabu = {}
    solucion_inicial, c = generate_initial_sol(graph)
    for _ in range(max_iter):
        vecindario, lista_tabu = generate_vecindario(graph, lista_tabu, solucion_inicial)
        menor_costo = float('inf')
        for v in vecindario:
            costo = path_cost(v, graph)
            if costo < menor_costo:
                menor_costo = costo
                mejor_camino = v
        solucion_inicial = mejor_camino
        c = menor_costo


    #*Limpiar output
    solucion = [int(a.replace('c', '')) for a in solucion_inicial]
    return solucion, c



if __name__ == '__main__':
    #Leemos input
    n_ciudades = int(input())
    n_max_iter = int(input())
    costos_cuidades = []
    for _ in range(n_ciudades - 1):
        costo = input()
        costo = [int(p) for p in costo.split()]
        costos_cuidades.append(costo)

    #Almacenamos el input como un grafo y se hace la búsqueda tabú
    dicc_graph = make_graph(costos_cuidades)
    r, c = busqueda_tabu(dicc_graph, n_max_iter)
    print('Solucion final')
    print(' '.join([str(a) for a in r]))
    print(c)
   
    
    