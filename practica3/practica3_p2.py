import statistics
from pe import evolucion

class Solucion:
    def __init__(self, s, v, p):
        self.solucion = s
        self.valor = v
        self.peso = p

def get_best_solution(solutions):
    best = sorted(solutions, key= lambda x: x[-1])
    return best[-1]

def get_worst_solution(solutions):
    best = sorted(solutions, key= lambda x: x[-1])
    return best[0]

def get_median(solutions):
    best = sorted(solutions, key= lambda x: x[-1])
    return best[len(solutions)//2]

def get_mean_cost(solutions):
    cont = 0
    for s in solutions:
        cont += -s[-1]
    return cont/len(solutions)

def get_sd_cost(solutions):
    valores = []
    for s in solutions:
        valores.append(s[-1])
    return statistics.stdev(valores)


if __name__ == '__main__':
    m = 5

    sols = []
    for i in range(m):
        solucion = evolucion(5,100,500,0.2,0.005)
        sols.append(solucion)

    print('*************************************** Mejor Solución ***************************************')
    mejor_sol = get_best_solution(sols)
    print(f'Xs = {mejor_sol[0]}')
    print(f'Sigmas = {mejor_sol[1]}')
    print(f'f(x) = {-mejor_sol[2]}')
    print('\n')

    print('*************************************** Peor Solución ***************************************')
    peor_sol = get_worst_solution(sols)
    print(f'Xs = {peor_sol[0]}')
    print(f'Sigmas = {peor_sol[1]}')
    print(f'f(x) = {-peor_sol[2]}')
    print('\n')

    print('******************************************* Mediana *******************************************')
    med_sol = get_median(sols)
    print(f'Xs = {med_sol[0]}')
    print(f'Sigmas = {med_sol[1]}')
    print(f'f(x) = {-med_sol[2]}')
    print('\n')

    print('Promedio:\t',get_mean_cost(sols))
    print('Stadard Dev:\t',get_sd_cost(sols))

    
