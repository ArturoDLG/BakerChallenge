import pygame as game
from utileria import Director
from Escenas.Escenarios import EscenaIntro, EscenaOpcion, EscenaJuego
from pygame import init

if __name__ == '__main__':
    director = Director()
    intro = EscenaIntro(director)
    opcion = EscenaOpcion(director)
    juego = EscenaJuego(director)

    director.change_scene(intro)
    director.loop()

    director.change_scene(opcion)
    director.loop()


