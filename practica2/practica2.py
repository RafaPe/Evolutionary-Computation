import random
import math
import copy

class Objeto:
    def __init__(self, v, p, i):
        self.valor = v
        self.peso = p
        self.indice = i


def generar_solucion_inicial(objetos, capacidad_mochila):
    solucion = [1 for _ in range(len(objetos))]
    capacidad_ocupada = sum([objeto.peso for objeto in objetos])
   
    while capacidad_ocupada > capacidad_mochila:
        objeto = random.sample(objetos, 1)[0]
        if capacidad_ocupada - objeto.peso > capacidad_mochila and solucion[objeto.indice] == 1:
            capacidad_mochila += objeto.peso
            solucion[objeto.indice] = 0
        elif capacidad_ocupada - objeto.peso <= capacidad_mochila and solucion[objeto.indice] == 1:
            capacidad_mochila += objeto.peso
            solucion[objeto.indice] = 0
            break

    return solucion
        
def evaluar_peso(solucion, objetos, capacidad):
    peso = 0
    for item in zip(solucion, objetos):
        if item[0] == 1:
            peso += item[1].peso
    return peso

def evaluar(solucion, objetos, capacidad):
    valor = 0
    for item in zip(solucion, objetos):
        if item[0] == 1:
            valor += item[1].valor
    return valor
    


def generar_vecindario(solucion, objetos, capacidad_mochila):
    vecindario = []
    for i in range(len(solucion)):
        if solucion[i] == 0:
            solucion[i] = 1
            if evaluar_peso(solucion, objetos, capacidad_mochila) <= capacidad_mochila:
                vecindario.append(copy.deepcopy(solucion))
            solucion[i] = 0
        elif solucion[i] == 1:
            solucion[i] = 0
            if evaluar_peso(solucion, objetos, capacidad_mochila) <= capacidad_mochila:
                vecindario.append(copy.deepcopy(solucion))
            solucion[i] = 1
    
    return vecindario
        
            

def recocido_simulado(objetos, capacidad_mochila, t_inicial, t_final):
    t = t_inicial
    solucion = generar_solucion_inicial(objetos, capacidad_mochila)
    while t > t_final:
        vecindario = generar_vecindario(solucion, objetos, capacidad_mochila)
        nueva_solucion = random.sample(vecindario, 1)[0]
        if evaluar(nueva_solucion, objetos, capacidad_mochila) > evaluar(solucion, objetos, capacidad_mochila):
            # print('Elegido por funcion')
            solucion = nueva_solucion
        else:
            if random.uniform(0, 1) < math.e**(-((evaluar(solucion, objetos, capacidad_mochila) - evaluar(nueva_solucion, objetos, capacidad_mochila))/t)):
                # print('Elegido por azar')
                solucion = nueva_solucion
        t = 0.99*t
        # print(solucion, evaluar(solucion, objetos, capacidad_mochila))
    return solucion, evaluar(solucion, objetos, capacidad_mochila)



if __name__ == '__main__':
    t_inicial, t_final = [float(a) for a in input().split()]
    n_objetos = int(input())
    capacidad = int(input())
    mochila = []
    for i in range(n_objetos):
        valor, peso = [int(a) for a in input().split()]
        mochila.append(Objeto(valor, peso, i))

    solucion, valor = recocido_simulado(mochila, capacidad, t_inicial, t_final)
    indexes, peso = [], 0
    for s in zip(solucion, mochila):
        if s[0] == 1:
            peso += s[1].peso
            indexes.append(s[1].indice)

    print(indexes, ''.join([str(a) for a in solucion]))
    print(valor)
    print(peso)

    
   
    
    