from Utileria import Director
from Escenas.Escenarios import EscenaIntro, EscenaJuego, EscenaGanador, EscenaContinuar

if __name__ == '__main__':
    director = Director()
    intro = EscenaIntro(director)
    ganador = EscenaGanador(director)
    continuar = EscenaContinuar(director)

    director.change_scene(intro)

    while continuar.respuesta_continuar:
        juego = EscenaJuego(director)
        juego.reproducir_musica()
        director.change_scene(juego)

        ganador.ganador = juego.tablero_virtual.ganador()
        director.change_scene(ganador)

        del juego

        director.change_scene(continuar)
