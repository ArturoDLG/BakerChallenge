from Utileria import Escenario, Boton, dibujar_texto
from Utileria import BLANCO, GRIS_OSCURO, NARANAJA, AZUL
from pygame import font, init, mixer
from MiniMax import Tablero, JugadorIA, JUGADOR, IA
from itertools import cycle

init()
fuente = font.Font("Escenas/media/Roboto-Regular.ttf", 20)
FUENTE_TITULOS = font.Font("Escenas/media/Roboto-Black.ttf", 80)
FUENTE_TITULOS_MINI = font.Font("Escenas/media/Roboto-Black.ttf", 60)
FUENTE_ETIQUETAS = font.Font("Escenas/media/Roboto-Regular.ttf", 80)
FUENTE_ETIQUETAS_MINI = font.Font("Escenas/media/Roboto-Regular.ttf", 50)


class EscenaIntro(Escenario):
    def __init__(self, director):
        Escenario.__init__(self, director)
        self.logotipo = Boton(100, 40, 300, 300, "Escenas/media/logo.png")
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
        dibujar_texto("#BakerChallenge", FUENTE_TITULOS_MINI,
                      self.director.screen, 20, 400, GRIS_OSCURO)


class EscenaJuego(Escenario):
    def __init__(self, director):
        Escenario.__init__(self, director)
        # Elementos de la interfaz del tablero
        self.fondo_tablero = Boton(0, 0, 150, 500, "Escenas/media/fondo_blanco.png")
        self.casilla1 = Boton(12.5, 162.5, 150, 150, "Escenas/media/fondo_blanco.png")
        self.casilla2 = Boton(175, 162.5, 150, 150, "Escenas/media/fondo_blanco.png")
        self.casilla3 = Boton(337.5, 162.5, 150, 150, "Escenas/media/fondo_blanco.png")
        self.casilla4 = Boton(12.5, 325, 150, 150, "Escenas/media/fondo_blanco.png")
        self.casilla5 = Boton(175, 325, 150, 150, "Escenas/media/fondo_blanco.png")
        self.casilla6 = Boton(337.5, 325, 150, 150, "Escenas/media/fondo_blanco.png")
        self.casilla7 = Boton(12.5, 487.5, 150, 150, "Escenas/media/fondo_blanco.png")
        self.casilla8 = Boton(175, 487.5, 150, 150, "Escenas/media/fondo_blanco.png")
        self.casilla9 = Boton(337.5, 487.5, 150, 150, "Escenas/media/fondo_blanco.png")
        self.casillas_validas = {0: self.casilla1, 1: self.casilla2, 2: self.casilla3,
                                 3: self.casilla4, 4: self.casilla5, 5: self.casilla6,
                                 6: self.casilla7, 7: self.casilla8, 8: self.casilla9}
        self.imagen_jugador = "Escenas/media/Tu.png"
        self.imagen_IA = "Escenas/media/Baker.png"
        self.marcador_jugador = Boton(50, 50, 75, 75, "Escenas/media/Tu.png")
        self.marcador_IA = Boton(375, 50, 75, 75, "Escenas/media/Baker.png")
        self.click = mixer.Sound("Escenas/media/click.ogg")
        self.musica_fondo = mixer.music.load("Escenas/media/Kick Shock.mp3")

        # Elementos del algoritmo MiniMax
        self.tablero_virtual = Tablero()
        self.jugador_IA = JugadorIA()
        self.turnos = cycle([JUGADOR, IA])
        self.turno = next(self.turnos)
        self.color_jugador = AZUL
        self.color_IA = AZUL
        self.iniciar_contador = False
        self.contador = 0
        self.contador_resultado = 0

    def actualizar(self):
        if self.iniciar_contador:
            self.contador += 1

        self.fin_del_juego()

        if self.turno == IA:
            self.color_jugador = AZUL
            self.color_IA = NARANAJA

        if self.turno == IA and self.contador == 10:
            self.click.play()
            mov = self.jugador_IA.realizar_movimiento(self.tablero_virtual, self.turno)
            self.casillas_validas[mov].imagen = self.imagen_IA
            self.casillas_validas.pop(mov)
            self.turno = next(self.turnos)
            self.contador = 0
            self.iniciar_contador = False

    def eventos(self, e):

        self.fin_del_juego()

        if self.turno == JUGADOR:
            self.color_jugador = NARANAJA
            self.color_IA = AZUL
            for mov, casilla in self.casillas_validas.items():
                if casilla.click(e):
                    self.click.play()
                    casilla.imagen = self.imagen_jugador
                    self.tablero_virtual.hacer_movimiento(mov, self.turno)
                    self.casillas_validas.pop(mov)
                    self.turno = next(self.turnos)
                    self.iniciar_contador = True
                    break

    def en_escena(self):
        self.director.screen.fill(GRIS_OSCURO)
        self.director.screen.blit(*self.fondo_tablero.imprimir())
        dibujar_texto("TU", FUENTE_ETIQUETAS_MINI, self.director.screen,
                      60, 0, self.color_jugador)
        self.director.screen.blit(*self.marcador_jugador.imprimir())
        dibujar_texto("BAKER", FUENTE_ETIQUETAS_MINI, self.director.screen,
                      340, 0, self.color_IA)
        self.director.screen.blit(*self.marcador_IA.imprimir())
        self.director.screen.blit(*self.casilla1.imprimir())
        self.director.screen.blit(*self.casilla2.imprimir())
        self.director.screen.blit(*self.casilla3.imprimir())
        self.director.screen.blit(*self.casilla4.imprimir())
        self.director.screen.blit(*self.casilla5.imprimir())
        self.director.screen.blit(*self.casilla6.imprimir())
        self.director.screen.blit(*self.casilla7.imprimir())
        self.director.screen.blit(*self.casilla8.imprimir())
        self.director.screen.blit(*self.casilla9.imprimir())

    def reproducir_musica(self):
        self.musica_fondo = mixer.music.play(-1, 0.0)

    def fin_del_juego(self):
        if self.tablero_virtual.fin_del_juego():
            mixer.music.stop()
            self.iniciar_contador = False
            self.contador_resultado += 1
            if self.contador_resultado == 75:
                self.director.quit_flag = True


class EscenaGanador(Escenario):
    def __init__(self, director):
        Escenario.__init__(self, director)
        self.ganador = None
        self.contador = 0
        self.tu = None
        self.baker = None

    def actualizar(self):
        self.contador += 1
        if self.contador == 75:
            self.contador = 0
            self.director.quit_flag = True

    def eventos(self, e):
        pass

    def en_escena(self):
        self.director.screen.fill(BLANCO)
        self.mostrar_ganador()
        if self.ganador == 'i':
            dibujar_texto("El ganador es", FUENTE_ETIQUETAS,
                          self.director.screen, 10, 75, GRIS_OSCURO)
            dibujar_texto("Baker", FUENTE_TITULOS,
                          self.director.screen, 150, 170, GRIS_OSCURO)
            self.director.screen.blit(*self.baker.imprimir())
        elif self.ganador == 'j':
            dibujar_texto("Ganaste", FUENTE_TITULOS,
                          self.director.screen, 100, 200, GRIS_OSCURO)
            self.director.screen.blit(*self.tu.imprimir())
        else:
            dibujar_texto("Empate", FUENTE_TITULOS,
                          self.director.screen, 100, 100, GRIS_OSCURO)
            self.director.screen.blit(*self.tu.imprimir())
            self.director.screen.blit(*self.baker.imprimir())

    def mostrar_ganador(self):
        if self.ganador == 'i':
            self.baker = Boton(150, 300, 200, 200, "Escenas/media/Baker.png")
        elif self.ganador == 'j':
            self.tu = Boton(150, 300, 200, 200, "Escenas/media/Tu.png")
        else:
            self.baker = Boton(50, 200, 200, 200, "Escenas/media/Baker.png")
            self.tu = Boton(250, 200, 200, 200, "Escenas/media/Tu.png")


class EscenaContinuar(Escenario):
    def __init__(self, director):
        Escenario.__init__(self, director)
        self.continuar = Boton(100, 270, 100, 100, "Escenas/media/aceptar.png")
        self.salir = Boton(300, 270, 100, 100, "Escenas/media/salir.png")
        self.respuesta_continuar = True

    def actualizar(self):
        pass

    def eventos(self, e):
        if self.continuar.click(e):
            self.director.quit_flag = True
        elif self.salir.click(e):
            self.respuesta_continuar = False
            self.director.quit_flag = True

    def en_escena(self):
        self.director.screen.fill(BLANCO)
        dibujar_texto("¿Desea", FUENTE_ETIQUETAS,
                      self.director.screen, 50, 75, GRIS_OSCURO)
        dibujar_texto("Continuar?", FUENTE_ETIQUETAS,
                      self.director.screen, 50, 160, GRIS_OSCURO)
        self.director.screen.blit(*self.continuar.imprimir())
        self.director.screen.blit(*self.salir.imprimir())
        dibujar_texto("SI", FUENTE_ETIQUETAS_MINI,
                      self.director.screen, 120, 380, GRIS_OSCURO)
        dibujar_texto("NO", FUENTE_ETIQUETAS_MINI,
                      self.director.screen, 320, 380, GRIS_OSCURO)
