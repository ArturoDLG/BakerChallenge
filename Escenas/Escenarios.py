from utileria import Escenario, Boton, dibujar_texto
from utileria import  BLANCO, NEGRO, AZUL
from pygame import font, init

init()
fuente = font.Font(None, 20)
FUENTE = font.SysFont(None, 125)

class EscenaIntro(Escenario):
    def __init__(self, director):
        Escenario.__init__(self,director)
        self. contador = 0

    def actualizar(self):
        self.contador +=1
        if self.contador == 200: self.director.quit_flag = True

    def eventos(self, e):
        pass

    def en_escena(self):
        self.director.screen.fill(BLANCO)


class EscenaOpcion(Escenario):
    def __init__(self, director):
        Escenario.__init__(self, director)
        self.BotonCruz = Boton(50, 50, 100, 100, "Escenas/media/x.png")
        self.BotonCirculo = Boton(100, 100, 100, 100, "Escenas/media/circulo.png")

    def actualizar(self):
        pass

    def eventos(self, e):
        pass

    def en_escena(self):
        self.director.screen.fill(AZUL)
        dibujar_texto("Elige Una Opción",
                      FUENTE, self.director.screen, 500, 500, BLANCO)
        self.director.screen.blit(*self.BotonCruz.imprimir())
        self.director.screen.blit(*self.BotonCirculo.imprimir())

class EscenaJuego(Escenario):
    def __init__(self, director):
        Escenario.__init__(self,director)

    def actualizar(self):
        pass

    def eventos(self, e):
        pass

    def en_escena(self):
        self.director.screen.fill(BLANCO)