import math
import time
import random
import copy

def vecino(estado):
    nuevo_estado = copy.deepcopy(estado)
    inicio_1 = random.randint(0,N-1)
    inicio_2 = random.randint(0,N-1)
    nuevo_estado[inicio_1]=inicio_2
    while nuevo_estado[inicio_1] == estado[inicio_1]:
        inicio_2 = random.randint(0,N-1)
        nuevo_estado[inicio_1]=inicio_2
    return nuevo_estado

def simulated_annealing(estado):
    alpha = 0.01
    contador_pasos = 0
    T = 1
    current = estado
    while T > 0 and calcula_objetivo(current)!=0:
        siguiente = vecino(current)
        delta_e = calcula_objetivo(current)-calcula_objetivo(siguiente)
        if  (random.uniform(0,1) < math.exp(delta_e / T) or (delta_e > 0)):
            current = siguiente
        T = T - alpha
        contador_pasos = contador_pasos +1
    
    print("Solucion Simulated Annealing: ",current)
    print("Total de reinas amenazadas: ",calcula_objetivo(current))
    print("Total de pasos: ",contador_pasos)
 

def calcula_objetivo(estado):
    contador = 0
    for i in range(0,N):
        for j in range(i+1,N):
            if estado[j]==estado[i]:
                contador = contador +1
            if estado[j]+j==estado[i]+i or estado[j]-j==estado[i]-i:
                contador = contador +1
    return contador

if __name__ == '__main__':
    start_time=time.time()
    N=8
    estado = [random.randint(0,N-1) for i in range(0,N)]
    print("Estado inicial ",estado)
    simulated_annealing(estado)
    end_time=time.time()
    ejec_time = end_time - start_time
    print("Tiempo de ejecución: ",ejec_time)
