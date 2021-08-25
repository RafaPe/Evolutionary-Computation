import numpy as np
import math
import copy
import random

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

def generar_poblacion_inicial(u, n):
    poblacion = []
    for _ in range(u):
        x_i = [np.random.uniform(-30, 30) for _ in range(n)]
        s_i = np.random.uniform(0, 1) 
        p = adecuacion(x_i)
        # s_i = sigma 
        poblacion.append([x_i, s_i, p])
    return poblacion

def elegir_padres(poblacion):
    return random.sample(poblacion, 1)[0], random.sample(poblacion, 1)[0]

def cruza(padres):
    padre1 = padres[0]
    padre2 = padres[1]
    hijo = []
    for i in range(len(padre1[0])):
        a = np.random.uniform(0,1)
        if a < 0.5:
            hijo.append(padre1[0][i])
        else:
            hijo.append(padre2[0][i])

    cruza = [hijo]
    a = np.random.uniform(0,1)
    if a < 0.5:
        cruza.append(padre1[1])
    else:
        cruza.append(padre2[1])

    p = adecuacion(cruza[0])
    cruza.append(p)

    return cruza


def mutacion(hijo, epsilon, tau):
    variables_mutadas = []
    sigma_n = hijo[1] * (math.e**((tau*np.random.normal(0,1))))
    if sigma_n < epsilon:
        sigma_n = epsilon
    for x in hijo[0]:
        x_i = x * (np.random.normal(0,1)*sigma_n)
        variables_mutadas.append(x_i)

    mutado = [variables_mutadas, sigma_n]
    mutado.append(adecuacion(variables_mutadas))
    return mutado

def generar_hijo(padres, epsilon, tau):
    cruza_ = cruza(padres)
    mutacion_ = mutacion(cruza_, epsilon, tau)
    return mutacion_

def evolucion(G, tau, epsilon, u, lambda_, n):
    poblacion = generar_poblacion_inicial(u, n)
    generaciones = 0
    while generaciones < G:
        cont = 0
        hijos = []
        while cont < lambda_:
            padres = elegir_padres(poblacion)
            hijo = generar_hijo(padres, epsilon, tau)
            hijos.append(hijo)
            cont += 1

        poblacion = sorted(hijos, key= lambda x: x[-1], reverse=True)
        poblacion = poblacion[:u]

        generaciones += 1

    return poblacion[-1]

if __name__ == '__main__':
    # p = generar_poblacion_inicial(5, 2)
    # for po in p:
    #     print(po)

    # padres = elegir_padres(p)
    # for p in padres:
    #     print(p)
    # print('------------------')
    # print(cruza(padres))
    print(evolucion(1000, 1/(math.sqrt(3)), 0.01, 30, 50, 3))