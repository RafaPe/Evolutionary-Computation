#Estrategias Evolutivas
import numpy as np
import math
import copy

def f(x):
    sumatoria1 = 0
    sumatoria2 = 0
    for x_ in x:
        sumatoria1 += x_**2
        sumatoria2 += math.cos(x_ * math.pi * 2)
    p1 = -20*(math.e**(-0.2*(math.sqrt(((1/len(x)*sumatoria1))))))
    p2 = -math.e**(((1/len(x))*sumatoria2))

    return p1 + p2 + 20 + math.e

def adecuacion(x):
    return -f(x)

def generar_solucion_inicial(n, sigma):
    x_i = [np.random.uniform(-30, 30) for _ in range(n)]
    # s_i = [np.random.normal(0, sigma)] 
    # s_i = sigma 
    return [x_i, sigma]

def mutacion(x, sigma):
    x_nueva = [i + (sigma * np.random.normal(0, 1)) for i in x[0]]
    return [x_nueva, sigma]

def evolucion(sigma, cons, G, num_vars):
    solucion = generar_solucion_inicial(num_vars, sigma)
    mejoras = 0
    i = 0
    while i < G:
        # print(i)
        # print(solucion, adecuacion(solucion[0]))
        nueva_solucion = mutacion(solucion, sigma)
        if adecuacion(nueva_solucion[0]) > adecuacion(solucion[0]):
            solucion = copy.deepcopy(nueva_solucion)
            mejoras += 1
        i += 1

        #Definí checar la relación de las mejoras cada 10 iteraciones
        if i % 5 == 0: 
            # print('checando mejoras  ', mejoras)
            p_s = mejoras/5
            if p_s > 1/5:
                sigma = sigma/cons
            elif p_s < 1/5:
                sigma = sigma * cons
            mejoras = 0
            # print('nueva sigma   ', sigma)

    return solucion
            

if __name__ == '__main__':
    # c = generar_solucion_inicial(3, 0.2)
    # b = mutacion(c)
    # print(c)
    # print(b)
    solucion = evolucion(0.5, 0.817, 50, 2)
    print(adecuacion(solucion[0]))
