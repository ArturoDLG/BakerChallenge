#!/usr/bin/env python

# -*- coding: iso-8859-15 -*-
# python-starcoIAtutorial:
# Codigo fuente implementando tres en raya con minimax
#
# copyright (C) 2008 Sergio Sanchez Mendez
# www.starcostudios.com/community/blog
#
# Este programa es software libre: usted puede redistribuirlo y/o modificarlo bajo los terminos de la Licencia
# Publica General GNU publicada por la Fundacion para el Software Libre, ya sea la version 3 de la Licencia,
# o (a su eleccion) cualquier version posterior. Este programa se distribuye con la esperanza de que sea util,
# pero SIN GARANTIA ALGUNA; ni siquiera la garantia implicita MERCANTIL o de APTITUD PARA UN PROPOSITO DETERMINADO.
# Consulte los detalles de la Licencia Publica General GNU para obtener una informacion mas detallada. Deberia haber
# recibido una copia de la Licencia Publica General GNU junto a este programa. En caso contrario,
# consulte <http://www.gnu.org/licenses/>.

from operator import itemgetter

# Constantes del tablero
VACIO = '-'  # Casilla Vacia
JUGADOR = 'j'  # Casilla del jugador
IA = 'i'  # Casilla de la IA


class Tablero:
    def __init__(self):
        """Crear el tablero virtual del tic tac toe"""
        self.casillas = [VACIO] * 9

    def movimientos_validos(self):
        """Retorna un generador de movimientos validos
        en el tablero"""
        return [pos for pos in range(9) if self.casillas[pos] == VACIO]

    def hacer_movimiento(self, movimiento, jugador):
        """Coloca una ficha en el tablero dependiendo
        el jugador"""
        self.casillas[movimiento] = jugador

    def deshacer_movimiento(self, movimiento):
        """Deshace un movimiento"""
        self.hacer_movimiento(movimiento, VACIO)

    def ganador(self):
        """Determinar el ganador del juego
        Retorna X si el ganador es el usuario
        Retorna O si el ganador es la IA
        Retorna None en caso de no haber ganador"""
        filas_ganadoras = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # vertical
                           [0, 3, 6], [1, 4, 7], [2, 5, 8],  # horizontal
                           [0, 4, 8], [2, 4, 6]]  # diagonal

        for fila in filas_ganadoras:
            jugador = fila[0]
            if self.casillas[jugador] != VACIO and Tablero.todos_iguales([self.casillas[i] for i in fila]):
                return self.casillas[jugador]

    def fin_del_juego(self):
        """Retorna si el juago a finalizado
        El juego finaliza si un jugador a ganado o
        no existen mas movimiento validos"""
        return self.ganador() or not self.movimientos_validos()

    @staticmethod
    def todos_iguales(lista):
        """Determinar que todos los elementos de la
        lista son iguales"""
        return not lista or lista == [lista[0]] * len(lista)


class JugadorIA:
    """Clase emuladora de la IA"""

    @staticmethod
    def realizar_movimiento(tablero, jugador):

        oponente = {JUGADOR: IA, IA: JUGADOR}

        def evaluar_movimiento(movimiento, j=jugador):
            """Evalua el mejor movimiento a realizar
            para poder ganar"""
            try:
                tablero.hacer_movimiento(movimiento, j)
                if tablero.fin_del_juego():
                    """Evalua la puntuacion del movimiento a realizar
                       Retorna 1 si la jugada lo hace ganar
                       Retorna 0 si la jugada no determina el juego
                       Retorna -1 si la jugada hace perder"""
                    return {jugador: 1, None: 0}.get(tablero.ganador(), -1)

                resultados = (evaluar_movimiento(sig_movimiento, oponente[j])
                              for sig_movimiento in tablero.movimientos_validos())

                if j == jugador:
                    min_elemento = 1
                    for r in resultados:
                        if r == -1:
                            return r
                        min_elemento = min(r, min_elemento)
                    return min_elemento

                else:
                    max_elemento = -1
                    for r in resultados:
                        if r == 1:
                            return r
                        max_elemento = max(r, max_elemento)
                    return max_elemento

            finally:
                tablero.deshacer_movimiento(movimiento)

        movimientos = [(movimiento, evaluar_movimiento(movimiento))
                       for movimiento in tablero.movimientos_validos()]
        movimiento = max(movimientos, key=itemgetter(1))[0]
        tablero.hacer_movimiento(movimiento, jugador)
        return movimiento
