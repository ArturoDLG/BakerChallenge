from Utileria import Escenario, Boton, dibujar_texto
from Utileria import  BLANCO, NEGRO, GRIS_OSCURO
from pygame import font, init
from MiniMax import Tablero, Jugador_IA, JUGADOR, IA
from Other_MiniMax import Board, jugadorMaquina, Jugador_O, Jugador_X
from itertools import cycle

init()
fuente = font.Font("Escenas/media/Roboto-Regular.ttf", 20)
FUENTE_TITULOS = font.Font("Escenas/media/Roboto-Black.ttf", 80)
FUENTE_ETIQUETAS = font.Font("Escenas/media/Roboto-Regular.ttf", 80)

class EscenaIntro(Escenario):
    def __init__(self, director):
        Escenario.__init__(self, director)
        self.logotipo = Boton(100,20,300,300,"Escenas/media/logo.png")
        self. contador = 0

    def actualizar(self):
        self.contador += 1
        if self.contador == 200:
            self.director.quit_flag = True

    def eventos(self, e):
        pass

    def en_escena(self):
        self.director.screen.fill(BLANCO)
        self.director.screen.blit(*self.logotipo.imprimir())
        dibujar_texto("Tic Tac Toe",FUENTE_TITULOS,
                      self.director.screen,50,350,GRIS_OSCURO)


class EscenaOpcion(Escenario):
    def __init__(self, director):
        Escenario.__init__(self, director)
        self.BotonCruz = Boton(30, 225, 205, 205, "Escenas/media/x.png")
        self.BotonCirculo = Boton(265, 225, 205, 205, "Escenas/media/circulo.png")

        # Variables para ls diguiente escena:
        self.imagen_jugador = None
        self.imagen_IA = None

    def actualizar(self):
        pass

    def eventos(self, e):
        if self.BotonCirculo.click(e):
            self.imagen_jugador = self.BotonCirculo.imagen
            self.imagen_IA = self.BotonCruz.imagen
            self.director.quit_flag = True

        elif self.BotonCruz.click(e):
            self.imagen_jugador = self.BotonCruz.imagen
            self.imagen_IA = self.BotonCirculo.imagen
            self.director.quit_flag = True

    def en_escena(self):
        self.director.screen.fill(BLANCO)
        dibujar_texto("Elige una", FUENTE_ETIQUETAS,
                      self.director.screen, 80, 0, GRIS_OSCURO)
        dibujar_texto("Opción", FUENTE_ETIQUETAS,
                      self.director.screen, 125, 90, GRIS_OSCURO)
        self.director.screen.blit(*self.BotonCruz.imprimir())
        self.director.screen.blit(*self.BotonCirculo.imprimir())


class EscenaJuego(Escenario):
    def __init__(self, director):
        Escenario.__init__(self, director)
        self.respuesta = True
        # self.tablero_virtual = Tablero()
        self.tablero_virtual = Board()
        self.fondo_tablero = Boton(0,0,150,500,"Escenas/media/fondo_blanco.png")
        self.casilla1 = Boton(12.5,162.5,150,150,"Escenas/media/fondo_blanco.png")
        self.casilla2 = Boton(175,162.5,150,150,"Escenas/media/fondo_blanco.png")
        self.casilla3 = Boton(337.5,162.5,150,150,"Escenas/media/fondo_blanco.png")
        self.casilla4 = Boton(12.5,325,150,150,"Escenas/media/fondo_blanco.png")
        self.casilla5 = Boton(175,325,150,150,"Escenas/media/fondo_blanco.png")
        self.casilla6 = Boton(337.5,325,150,150,"Escenas/media/fondo_blanco.png")
        self.casilla7 = Boton(12.5,487.5,150,150,"Escenas/media/fondo_blanco.png")
        self.casilla8 = Boton(175,487.5,150,150,"Escenas/media/fondo_blanco.png")
        self.casilla9 = Boton(337.5,487.5,150,150,"Escenas/media/fondo_blanco.png")
        self.casillas_validas = {0: self.casilla1, 1: self.casilla2, 2: self.casilla3,
                                 3: self.casilla4, 4: self.casilla5, 5: self.casilla6,
                                 6: self.casilla7, 7: self.casilla8, 8: self.casilla9}
        self.imagen_jugador = None
        self.imagen_IA = None
        # self.jugador_IA = Jugador_IA()
        # self.turnos = cycle([JUGADOR, IA])
        self.turnos = cycle([Jugador_X, Jugador_O])
        self.turno = next(self.turnos)
        self.iniciar_contador = False
        self.contador = 0

    def actualizar(self):
        if self.iniciar_contador:
            self.contador += 1

        self.fin_del_juego()

        if self.turno == Jugador_O and self.contador == 15:
            # self.jugador_IA.realizar_movimiento(self.tablero_virtual, self.turno)
            # mov = self.jugador_IA.movimiento
            mov = jugadorMaquina(self.tablero_virtual, self.turno )
            self.casillas_validas[mov].imagen = self.imagen_IA
            self.casillas_validas.pop(mov)
            self.turno  = next(self.turnos)
            self.contador = 0
            self.iniciar_contador = False

    def eventos(self, e):
        if self.turno == Jugador_X:
            for mov, casilla in self.casillas_validas.items():
                if casilla.click(e):
                    casilla.imagen = self.imagen_jugador
                    self.tablero_virtual.makeMove(mov, self.turno)
                    self.casillas_validas.pop(mov)
                    self.turno = next(self.turnos)
                    self.iniciar_contador = True
                    break

    def en_escena(self):
        self.director.screen.fill(GRIS_OSCURO)
        self.director.screen.blit(*self.fondo_tablero.imprimir())
        self.director.screen.blit(*self.casilla1.imprimir())
        self.director.screen.blit(*self.casilla2.imprimir())
        self.director.screen.blit(*self.casilla3.imprimir())
        self.director.screen.blit(*self.casilla4.imprimir())
        self.director.screen.blit(*self.casilla5.imprimir())
        self.director.screen.blit(*self.casilla6.imprimir())
        self.director.screen.blit(*self.casilla7.imprimir())
        self.director.screen.blit(*self.casilla8.imprimir())
        self.director.screen.blit(*self.casilla9.imprimir())

    def fin_del_juego(self):
        if self.tablero_virtual.gameOver():
            self.director.quit_flag = True

