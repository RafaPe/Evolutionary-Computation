import sys
import statistics
import matplotlib.pyplot as plt
plt.style.use('dark_background')
from practica1 import busqueda_tabu, make_graph

class Solucion:
    def __init__(self, p, c):
        self.camino = p
        self.costo = c

def get_best_solution(solutions):
    best = float('inf')
    for s in solutions:
        if s.costo < best:
            best = s.costo
            camino = s.camino
    return camino, best

def get_worst_solution(solutions):
    best = 0
    for s in solutions:
        if s.costo > best:
            best = s.costo
            camino = s.camino
    return camino, best

def get_median(solutions):
    mid = len(solutions)//2
    sols_sorted = sorted(solutions, key=lambda x: x.costo, reverse=False)
    return sols_sorted[mid].camino, sols_sorted[mid].costo

def get_mean_cost(solutions):
    cont = 0
    for s in solutions:
        cont += s.costo
    return cont/len(solutions)

def get_sd_cost(solutions):
    costs = []
    for s in solutions:
        costs.append(s.costo)
    return statistics.stdev(costs)


if __name__ == '__main__':
    input_file = sys.argv[1]
    m = int(sys.argv[2])
    costos_cuidades = []
    with open(input_file) as f:
        i = 0
        for line in f:
            if i == 0:
                n_ciudades = int(line)
            elif i == 1:
                max_iter = int(line)
            else:
                costo = line
                costo = [int(p) for p in costo.split()]
                costos_cuidades.append(costo)
            i += 1

    sols = []
    graph = make_graph(costos_cuidades)
    for i in range(m):
        solucion, costo = busqueda_tabu(graph, max_iter)
        p = Solucion(solucion, costo)
        sols.append(p)

    print('Mejor Solución:\t', get_best_solution(sols))
    print('Peor Solución:\t',get_worst_solution(sols))
    print('Mediana:\t',get_median(sols))
    print('Promedio:\t',get_mean_cost(sols))
    print('Stadard Dev:\t',get_sd_cost(sols))

    
    ''' Graficar Resultados '''
    # costos = []
    # for s in sols:
    #     costos.append(s.costo)
    # x = [i for i in range(len(sols))]
    # plt.plot(x, costos, marker = 'o')
    # plt.ylabel('Busqueda Tabú Resultado')
    # plt.xlabel('Ejecuciones')
    # plt.show()