import numpy as np
import math

class Node:
    def __init__(self, padre=None, posicion=None):
        self.padre = padre
        self.posicion = posicion

        self.g = 0
        self.h = 0
        self.f = 0
        
    def __eq__(self, other):
        return (self.posicion) == other.posicion

def encontrar_ruta(nodo_actual,recorrido): # Encontrar la ruta que se esta buscando 
    ruta = []
    s_filas, s_columnas = np.shape(recorrido)

    resultado = [['X' for i in range(s_columnas)] for j in range(s_filas)] # Rellena con X
    
    current = nodo_actual 
    while current is not None:
        ruta.append(current.posicion)
        current = current.padre
    ruta = ruta[::-1] # invertir la ruta
    comienzo = 0
    
    for i in range(len(ruta)):
        resultado[ruta[i][0]][ruta[i][1]] = '-' # marca con '-' el camino que va recorriendo
        comienzo += 1
    
    if resultado != None:
        print('Camino: ',ruta)
        print('')
        return resultado

def buscar(recorrido, costo, inicio, fin):
    inicia_nodo = Node(None, tuple(inicio))
    inicia_nodo.g = inicia_nodo.h = inicia_nodo.f = 0
    finaliza_nodo = Node(None, tuple(fin))
    finaliza_nodo.g = finaliza_nodo.h = finaliza_nodo.f = 0

    lista_abierta = [] # lista con nodos por explorar
    
    lista_cerrada = [] # lista con los nodos ya verificados
    
    lista_abierta.append(inicia_nodo) # nodo inicial
    
    contador = 0 # contador de parada 
    maximo = (len(recorrido) // 2) ** 10 # maximo permitido
    
    # movimientos permitidos
    movimientos  =  [[-1, 0 ], # arriba
              [ 0, -1], # izquierda
              [ 1, 0 ], # abajo
              [ 0, 1 ]] # derecha
   
    s_filas, s_columnas = np.shape(recorrido) # cuantas filas y columnas
    
    while len(lista_abierta) > 0:
        contador = contador + 1
        nodo_actual = lista_abierta[0]
        indice_actual = 0
        for indice, info_actual in enumerate(lista_abierta):
            if info_actual.f < nodo_actual.f:
                nodo_actual = info_actual
                indice_actual = indice
        lista_abierta.pop(indice_actual) # retiro el nodo de la lista abierta
        lista_cerrada.append(nodo_actual) # coloco el nodo de la lista abierta en la cerrada significa que tiene
                                        # una frontera

        if nodo_actual == finaliza_nodo:
            return encontrar_ruta(nodo_actual,recorrido) # retorna la ruta encontrada
        hijos = [] 

        for nueva_posicion in movimientos: 
            posicion_nodo = (nodo_actual.posicion[0] + nueva_posicion[0], nodo_actual.posicion[1] + nueva_posicion[1])
            if (posicion_nodo[0] > (s_filas - 1) or  
                posicion_nodo[0] < 0 or 
                posicion_nodo[1] > (s_columnas -1) or 
                posicion_nodo[1] < 0): # verifica que esta dentro de la matriz
                continue
            if recorrido[posicion_nodo[0]][posicion_nodo[1]] != 0:
                continue
            nodo_nuevo = Node(nodo_actual, posicion_nodo) # crea un nuevo nodo
            hijos.append(nodo_nuevo)
        for hijo in hijos: # recorrer toda la lista de hijos
            if len([lista_hijo for lista_hijo in lista_cerrada if lista_hijo == hijo]) > 0:
                continue

            hijo.g = nodo_actual.g + costo # calculo el costo en g
            
            hijo.h = (((hijo.posicion[0] - finaliza_nodo.posicion[0]) ** 2) + 
                       ((hijo.posicion[1] - finaliza_nodo.posicion[1]) ** 2)) # Calcula el costo de heuristica

            hijo.f = hijo.g + hijo.h # calcula el valor de f
            if len([i for i in lista_abierta if hijo == i and hijo.g > i.g]) > 0: # el costo g es menor
                continue

            lista_abierta.append(hijo) # se agrega el hijo a la lista abierta


if __name__ == '__main__':

    recorrido = np.random.randint(0, 2, (10, 10))
    
    inicio = [2, 6] # posicion inicial
    fin = [4,2] # posicion final
    costo = 1 # costo del movimiento

    respuesta =(buscar(recorrido,costo, inicio, fin))
    while respuesta==None:
        recorrido = np.random.randint(0, 2, (10, 10))
        respuesta =buscar(recorrido,costo, inicio, fin)  
    print('Ambiente inicial: ')
    print('')
    for i in range(len(recorrido)):
        for j in range(len(recorrido)):
            print("|",(recorrido[i][j]),end=' ')    
        print("|")
    
    print('')
    print('Ambiente final: ')
    print('')
    for i in range(len(respuesta)):
        for j in range(len(respuesta)):
            print("| ",(respuesta[i][j]),end=' ')    
        print("|")    
