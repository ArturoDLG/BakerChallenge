# \#BakerChallenge (Proyecto Inteligencia Artificial)
___
## Objetivo
Implementar un juego de Tic Tac Toe utilizando el algoritmo MiniMax para lograr ganar un juego contra un adversario humano de la manera más rápida posible; como proyecto final para la clase de Inteligencia Artificial.

## Algoritmo MiniMax
El algoritmo de minimax en simples palabras consiste en la elección del mejor movimiento para el computador, suponiendo que el contrincante escogerá uno que lo pueda perjudicar, para escoger la mejor opción este algoritmo realiza un árbol de búsqueda con todos los posibles movimientos, luego recorre todo el árbol de soluciones del juego a partir de un estado dado, es decir, según las casillas que ya han sido rellenadas. Por tanto, minimax se ejecutará cada vez que le toque mover a la IA.

En el algoritmo Minimax el espacio de búsqueda queda definido por:

**Estado inicial:** Es una configuración inicial del juego, es decir, un estado en el que se encuentre el juego. 

**Operadores:** Corresponden a las jugadas legales que se pueden hacer en el juego.

**Condición Terminal:** Determina cuando el juego se acabó.

**Función de Utilidad:** Da un valor numérico a una configuración final de un juego. En un juego en donde se puede ganar, perder o empatar, los valores pueden ser 1, 0, o -1.  

**Implementación Minimax:** Los pasos que sigue minimax pueden variar, pero lo importante es tener una idea clara de cómo es su funcionamiento, los pasos a seguir son:

 * El algoritmo primero generar un árbol de soluciones completo a partir de un nodo dado.

* Para cada nodo final, buscamos la función de utilidad de estos. En nuestro ejemplo usaremos un 0 para las partidas que terminen en empate, un 1 para las que gane la IA y un -1 para las que gane el jugador humano. *Nota: Para obtener el camino más corto, se divide 1 entre la profundidad del árbol, asi los caminos mas cortos (de menor profundidad) darán mayor valor y los caminos mas cortos un menor valor. 

Y lo que hará el algoritmo Minimax cuando vaya regresando hacia atrás, será comunicarle a la llamada recursiva superior cuál es el mejor nodo hoja alcanzado hasta el momento. Cada llamada recursiva tiene que saber a quién le toca jugar, para analizar si el movimiento realizado pertenece a la IA o al otro jugador, ya que cuando sea el turno de la IA nos interesa MAXIMIZAR el resultado, y cuando sea el turno del rival MINIMIZAR su resultado.

Al final el algoritmo nos devolverá la jugada que debe realizar la máquina para maximizar sus posibilidades y bloquear las posibilidades del rival.

[Referencia: https://devcode.la/tutoriales/algoritmo-minimax/](https://devcode.la/tutoriales/algoritmo-minimax/)

## Herramientas utilizadas
Para desarrollo del proyecto se empleó Python; utilizando el modulo de videojuegos Pygame, un modulo propio con clases para crear botones, y manejo de escenas con la clase Director y la interfaz Escenas basabas en las implementadas en el sitio [razonartificial.com](http://razonartificial.com/2010/08/gestionando-escenas-con-pygame/) y un modulo con el algoritmo MiniMax, con el codigo obtenido de [starcostudios.com](www.starcostudios.com/community/blog) modificado para obtener el camino más corto mediante una división entre la profundidad de búsqueda de las posibilidades de ganar, siendo esta la heuristica propuesta.
