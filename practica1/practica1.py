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

def generate_initial_sol(graph):
    initial_sol = ['c0']
    cost = 0
    ciudad_inicial = 'c0'
    
    while len(initial_sol) < 10:
        # print('-----------------------------------------------')
        # print('Cuidad actual: ' + ciudad_inicial)
        cuidad_menor_costo = ''
        menor = float('inf')
        for city in graph[ciudad_inicial]:
            # print(city, graph[ciudad_inicial][city])
            if graph[ciudad_inicial][city] < menor and city not in initial_sol:
                # print('Este fue el menor hasta ahora')
                menor = graph[ciudad_inicial][city]
                cuidad_menor_costo = city
                # print(menor, cuidad_menor_costo)
        cost += menor
        ciudad_inicial = cuidad_menor_costo
        initial_sol.append(ciudad_inicial)
    
    cost += graph[initial_sol[-1]]['c0']

    return initial_sol, cost

def generate_vecindario(graph, lista_tabu, s):
    eliminate = []
    for k in lista_tabu:
        if lista_tabu[k] == 0:
            eliminate.append(k)
    for e in eliminate:
        lista_tabu.pop(e)
    for k in lista_tabu:
        lista_tabu[k] = lista_tabu[k] - 1

    vecindario = []
    p = random.randint(1,len(s)-1)
    while s[p] in lista_tabu:
        p = random.randint(1,len(s)-1)
    # print('ciudad a cambiar: ', s[p])
    if s[p] not in lista_tabu:
        for i in range(1,len(s)):
            if i == p:
                continue
            else:
                s2 = copy.deepcopy(s)
                a, b = s[i], s[p]
                s2[i], s2[p] = b, a
                vecindario.append(s2)
        lista_tabu[s[p]] = len(graph)//2
    return vecindario, lista_tabu

def path_cost(camino, graph):
    cost = 0
    for i in range(len(camino)-2):
        a, b = camino[i], camino[i+1]
        cost += graph[a][b]
        # print(a, '->', b)
        # print('costo', graph[a][b])
        # print('total acumulado', cost)
    cost += graph[camino[-1]]['c0']

    return cost

def busqueda_tabu(graph, max_iter):
    lista_tabu = {}
    solucion_inicial, c = generate_initial_sol(graph)
    # print('Solucion inicial greedy')
    # print(solucion_inicial, c)
    # print('\n')
    for _ in range(max_iter):
        # print('lista tabu: ', lista_tabu)
        vecindario, lista_tabu = generate_vecindario(graph, lista_tabu, solucion_inicial)
        # for v in vecindario:
        #     print(v)
        menor_costo = float('inf')
        # mejor_camino = []
        for v in vecindario:
            costo = path_cost(v, graph)
            # print(v, costo)
            if costo < menor_costo:
                menor_costo = costo
                mejor_camino = v
        solucion_inicial = mejor_camino
        c = menor_costo
        # print('Nueva solucion')
        # print(solucion_inicial, c)

    #**Limpiar output
    solucion = [int(a.replace('c', '')) for a in solucion_inicial]
    return solucion, c
        
    
    # print('solucion inicial')
    # print(solucion_inicial, c)
    # for v in vecindario:
    #     print(v)


if __name__ == '__main__':
    n_ciudades = int(input())
    n_max_iter = int(input())
    costos_cuidades = []
    for _ in range(n_ciudades - 1):
        costo = input()
        costo = [int(p) for p in costo.split()]
        costos_cuidades.append(costo)

    #TODO faltan los pesos de regreso
    dicc_graph = make_graph(costos_cuidades)
    #TODO esto arregla el problema anterior, implementarlo en la función
    # dicc_graph['c1']['c0'] = dicc_graph['c0']['c1']
    # print(dicc_graph)
    # for dic in dicc_graph:
    #     print(dic, '---' , dicc_graph[dic])
    r, c = busqueda_tabu(dicc_graph, n_max_iter)
    print('Solucion final')
    print(' '.join([str(a) for a in r]))
    print(c)
   
    
    