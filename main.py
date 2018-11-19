from Utileria import Director
from Escenas.Escenarios import EscenaIntro, EscenaOpcion, EscenaJuego
from itertools import  cycle

if __name__ == '__main__':
    director = Director()
    intro = EscenaIntro(director)
    opcion = EscenaOpcion(director)
    juego = EscenaJuego(director)

    director.change_scene(intro)
    director.loop()

    director.change_scene(opcion)
    director.loop()

    juego.imagen_jugador = opcion.imagen_jugador
    juego.imagen_IA = opcion.imagen_IA

    director.change_scene(juego)
    director.loop()
