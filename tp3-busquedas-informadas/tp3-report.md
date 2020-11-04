## Problema a resolver.

El problema que se lleva a cabo es el analisis de un agente que tiene que realizar una tarea que consiste en lo siguiente:
- Crear una matriz con casillas libre y casillas con objetos
- Esas casillas en el problema son representada inicialmente con 0 y 1
- La matriz con casillas libre y ocupadas es random 
- Se le da al problema un punto de partida
- Se le da al problema un punto destino

El agente lo que tiene que realizar es llegar desde un punto inicio hasta un punto destino.
El agente se basa en objetivo, ya que necesita un punto de inicio hasta el punto de partida.
Durante el proceso de resolucion tiene que analizar si tiene obstaculos, para ello lo que hace es lo siguiente:
- Se define el punto de partida.
- De ese punto de partida analiza 4 posibilidades arriba, abajo, izquierda y derecha, de la casilla que se encuentra
- Cada vez que analiza los que hace es a traves de una formula colocar un valor
- La formula es la siguiente f = g +h
- Donde h es la huristica que tiene la siguiente forma: (Xinicial -Xfinal)^2 + (Yinicial - Yfinal)^2
- Siendo g el costo
- Tomando estos valores (g y h) obtenemos f
- Con f lo que vamos a hacer es tomar deciciones para le mejor camin
- El algoritmo se encarga de resolver todas las situaciones y llegar al destino.
