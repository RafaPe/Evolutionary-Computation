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
    #La adecuación es la función en negativo porque queremos encontrar el mínimo local
    return -f(x)
    
def poblacion_inicial(mu, n):
    '''n es la cantidad de valores de una solución 
        ej [x1,x2,x3,s1,s2,s3] tiene 3 soluciones'''
    padres = []
    for _ in range(mu):
        x = list(np.random.uniform(-30, 30, n))
        sigmas = list(np.random.uniform(0, 1, n))
        # p = list(zip(np.random.uniform(-30, 30, n), np.random.uniform(0, 1, n)))
        p = [x, sigmas]
        p.append(adecuacion(p[0]))
        padres.append(p)
    
    return padres

def mutacion(padre, n, alpha, epsilon):
    hijo = copy.deepcopy(padre)
    # hijo[0][0], hijo[0][1] = list(hijo[0][0]), list(hijo[0][1])
    # print(hijo)
    for i in range(len(hijo[1])):
        hijo[1][i] = alpha*np.random.normal(0,1,1)[0]
        if hijo[1][i] < epsilon:
            hijo[1][i] = epsilon
    for i in range(len(hijo[0])):
        hijo[0][i] = hijo[0][i] + hijo[1][i]*np.random.normal(0,1,1)[0]
        if hijo[0][i] <-30:
            hijo[0][i] = -30
        elif hijo[0][i] > 30:
            hijo[0][i] = 30
    # print(hijo[0])
    hijo[2] = adecuacion(hijo[0])
    return hijo
    
            

        
def evolucion(n, mu, generaciones, alpha, epsilon = 0.01):
    padres = poblacion_inicial(mu, n)

    for _ in range(generaciones):
        generacion = copy.deepcopy(padres)
        for p in padres:
            hijo = mutacion(p, n, alpha, epsilon)
            generacion.append(hijo)
        generacion = sorted(generacion, key= lambda x: x[-1])
        seleccion = generacion[mu:]
        padres = copy.deepcopy(seleccion)

    return padres[-1]

        
    

if __name__ == '__main__':
    # # print(f([0,0]))
    # p = poblacion_inicial(2,2)
    # for t in p:
    #     # print(p)
    #     print(mutacion(t,2,0.2,0.01))
    # print(evolucion(3,100,2000,0.2,0.005))
    # print(len(poblacion_inicial(1,4)[0][1]))
    v = int(input())
    mu, gens = [int(a) for a in input.split()]
    alpha, epsilon = [int(a) for a in input.split()]
    print(evolucion(v,mu,gens,alpha,epsilon))
