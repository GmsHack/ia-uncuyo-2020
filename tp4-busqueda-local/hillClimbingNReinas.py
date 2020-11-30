import random
import time

def conflictos(estado):
	cantidad = 0
	for i in range(len(estado)):
		for j in range(i + 1,len(estado)):
			if estado[i] == estado[j]:
				cantidad = cantidad +1
			fuera_rango = j - i
			if abs(estado[i]-estado[j]) == fuera_rango:
				cantidad = cantidad+1
	return cantidad
def  hill_climbing(estado):
    convertir = {}
    longitud = len(estado)
    for columna in range(longitud):
            best_move = estado[columna]
            for fila in range(longitud):
                    if estado[columna] == fila:
                            continue
                    estado_copia = list(estado)
                    estado_copia[columna] = fila
                    convertir[(columna,fila)] = conflictos(estado_copia)
 
    respuesta = [] 
    conflicto_actual = conflictos(estado)
 
    for key,value in convertir.iteritems():
            if value < conflicto_actual:
                    conflicto_actual = value
    for key,value in convertir.iteritems():
            if value == conflicto_actual:
                    respuesta.append(key)
 
    if len(respuesta) > 0:
            i = random.randint(0,len(respuesta)-1)
            columna = respuesta[i][0]
            fila = respuesta[i][1]
            estado[columna] = fila
 
    return estado
 

def Queens():
    estado = [0,1,2,3,4,5,6,7,8,9]
    while conflictos(estado) > 0:
            estado = hill_climbing(estado)
            print estado
            print conflictos(estado)
    print "Solucion"
    print
    print estado
 
if __name__ == '__main__':
    start_time=time.time()
    Queens()
    end_time=time.time()
    ejec_time = end_time - start_time
    print("Tiempo de ejecucion: ",ejec_time)