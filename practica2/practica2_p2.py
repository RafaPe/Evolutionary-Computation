import sys
import statistics
import matplotlib.pyplot as plt
plt.style.use('dark_background')
from practica2 import recocido_simulado

class Objeto:
    def __init__(self, v, p, i):
        self.valor = v
        self.peso = p
        self.indice = i

class Solucion:
    def __init__(self, s, v, p):
        self.solucion = s
        self.valor = v
        self.peso = p

def get_best_solution(solutions):
    best = 0
    for s in solutions:
        if s.valor > best:
            best = s.valor
            sol = s.solucion
            w = s.peso
    return sol, best, w

def get_worst_solution(solutions):
    best = float('inf')
    for s in solutions:
        if s.valor < best:
            best = s.valor
            sol = s.solucion
            w = s.peso
    return sol, best, w

def get_median(solutions):
    mid = len(solutions)//2
    sols_sorted = sorted(solutions, key=lambda x: x.valor, reverse=False)
    return sols_sorted[mid].solucion, sols_sorted[mid].valor, sols_sorted[mid].peso

def get_mean_cost(solutions):
    cont = 0
    for s in solutions:
        cont += s.valor
    return cont/len(solutions)

def get_sd_cost(solutions):
    valores = []
    for s in solutions:
        valores.append(s.valor)
    return statistics.stdev(valores)


if __name__ == '__main__':
    input_file = sys.argv[1]
    m = int(sys.argv[2])
    mochila = []
    with open(input_file) as f:
        i = 0
        for line in f:
            if i == 0:
                t_inicial, t_final = [float(a) for a in line.split()]
            elif i == 1:
                n_objetos = int(line)
            elif i == 2:
                capacidad = int(line)
            else:
                valor, peso = [int(a) for a in line.split()]
                mochila.append(Objeto(valor, peso, i-3))
            i += 1


    sols = []
    # graph = make_graph(costos_cuidades)
    for i in range(m):
        solucion, valor = recocido_simulado(mochila, capacidad, t_inicial, t_final)
        peso = 0
        for s in zip(solucion, mochila):
            if s[0] == 1:
                peso += s[1].peso
        p = Solucion(solucion, valor, peso)
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