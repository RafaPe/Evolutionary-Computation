import numpy as np
import math
import copy
import random

class Hijo:
    def __init__(self, v, s, p, e):
        self.variables = v
        self.sigma = s
        self.adecuacion = p
        self.edad = e

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
        poblacion.append(Hijo(x_i, s_i, p, 0))
    return poblacion


def elegir_padres(poblacion):
    return random.sample(poblacion, 1)[0], random.sample(poblacion, 1)[0]

def cruza(padres):
    padre1 = padres[0]
    padre2 = padres[1]
    hijo = []
    for i in range(len(padre1.variables)):
        a = np.random.uniform(0,1)
        if a < 0.5:
            hijo.append(padre1.variables[i])
        else:
            hijo.append(padre2.variables[i])

    cruza = [hijo]
    a = np.random.uniform(0,1)
    if a < 0.5:
        cruza.append(padre1.sigma)
    else:
        cruza.append(padre2.sigma)

    p = adecuacion(cruza[0])
    # cruza.append(p)

    return Hijo(cruza[0], cruza[1], p, 0)

def mutacion(hijo, epsilon, tau):
    variables_mutadas = []
    sigma_n = hijo.sigma * (math.e**((tau*np.random.normal(0,1))))
    if sigma_n < epsilon:
        sigma_n = epsilon
    for x in hijo.variables:
        x_i = x * (np.random.normal(0,1)*sigma_n)
        variables_mutadas.append(x_i)

    mutado = [variables_mutadas, sigma_n]
    mutado.append(adecuacion(variables_mutadas))
    return Hijo(mutado[0], mutado[1], mutado[2], 0)

def generar_hijo(padres, epsilon, tau):
    cruza_ = cruza(padres)
    mutacion_ = mutacion(cruza_, epsilon, tau)
    return mutacion_

def evolucion(G, tau, epsilon, u, lambda_, n, age):
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
        poblacion = poblacion + hijos
        poblacion = sorted(poblacion, key= lambda x: x.adecuacion, reverse=True)
        poblacion = poblacion[:u]

        cont_ = 0
        for p in poblacion:
            p.edad = p.edad + 1
            if p.edad >= age and cont_ != 0:
                poblacion.remove(p)
            cont_ += 1
        
        faltan = u - len(poblacion)
        # print('faltan', faltan)
    
        if faltan > 0:
            poblacion = poblacion + generar_poblacion_inicial(faltan, n)

        # poblacion = sorted(poblacion, key= lambda x: x.adecuacion, reverse=True)

        generaciones += 1

    return poblacion[0]

if __name__ == '__main__':
    # p = generar_poblacion_inicial(5, 2)
    # for po in p:
    #     print(po)

    # padres = elegir_padres(p)
    # for p in padres:
    #     print(p)
    # print('------------------')
    # print(cruza(padres))
    respuesta = evolucion(1000, 1/(math.sqrt(3)), 0.01, 30, 50, 3, 10)
    print(respuesta.variables, respuesta.adecuacion, respuesta.edad)
