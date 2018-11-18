# paquete para manejo de clases para el proyecto

from pygame import display, time, event, mouse, font
from pygame import Rect as Rectangulo, image, transform
from pygame import MOUSEBUTTONDOWN, QUIT, KEYDOWN, K_ESCAPE, FULLSCREEN
from abc import ABCMeta, abstractmethod

# Constantes
BLANCO = 255, 255, 255,
NEGRO = 0, 0, 0,
AZUL = 0, 0, 255,



# Funciones
def dibujar_texto(texto, fuente, superficie, x, y, COLOR):
    objetotexto = fuente.render(texto, 1, COLOR)
    rectangulotexto = objetotexto.get_rect()
    rectangulotexto.topleft = (x, y)
    superficie.blit(objetotexto, rectangulotexto)

# Clases
class Boton(object):
    """Clase para implementar botones en Pygame"""

    def __init__(self, x, y, alto, ancho, imagen=None):
        """Constructor de la clase Boton
        -x: posicion en el eje de las X
        -y: posicion en el eje de las Y
        -alto: alto del boton
        -ancho: ancho del boton
        -imagen: archivo de imagen para darle un aspecto al boton"""

        self.__rectangulo = Rectangulo(x, y, ancho, alto)
        self.__imagen_archivo = imagen
        self.__imagen = transform.scale(image.load(self.__imagen_archivo), (ancho, alto))

    @property
    def posicion(self):
        """Metodo para obtener la posicion del boton en una tupla"""
        return self.__rectangulo.x, self.__rectangulo.y,

    @posicion.setter
    def posicion(self, pos_x=None, pos_y=None):
        """Metodo para modificar la posicion del boton"""
        if not pos_x == None:
            self.__rectangulo.x = pos_x
        if not pos_y == None:
            self.__rectangulo.y = pos_y

    @property
    def dimension(self):
        """Metodo para obtener la dimension del boton en un tupla"""
        return self.__rectangulo.height, self.__rectangulo.width,

    @dimension.setter
    def dimension(self, alto=None, ancho=None):
        """Metodo para modificar la dimension del boton"""
        if not alto == None:
            self.__rectangulo.height = alto
        if not ancho == None:
            self.__rectangulo.width = ancho

    @property
    def imagen(self):
        return self.__imagen_archivo

    @imagen.setter
    def imagen(self, nueva_imagen):
        self.__imagen_archivo = nueva_imagen
        self.__imagen = transform.scale(image.load(nueva_imagen), self.dimension[::-1])

    def imprimir(self):
        return self.__imagen, self.__rectangulo

    def click(self, evento_mouse):
        """Metodo privado para comprobar si el usuario
        realizo un click en el boton"""
        if evento_mouse == MOUSEBUTTONDOWN:
            if self.__rectangulo.collidepoint(mouse.get_pos()):
                return True
        return False


class Escenario(metaclass=ABCMeta):
    """Interfaz para la implementacion de escenas del juego"""

    def __init__(self, director):
        self.director = director

    @abstractmethod
    def actualizar(self):
        """Metodo para actualizar la escena"""
        pass

    @abstractmethod
    def eventos(self, e):
        """metodo para los eventos del juego"""
        pass

    @abstractmethod
    def en_escena(self):
        """Metodo para mostrar en pantalla
        los elementos en escena"""
        pass


class Director(object):
    """Clase director"""

    def __init__(self):
        self.screen = display.set_mode((0, 0), FULLSCREEN)
        display.set_mode((0, 0), FULLSCREEN)
        display.set_caption("Tic Tac Toe")
        self.scene = None
        self.quit_flag = False
        self.clock = time.Clock()

    def loop(self):
        "Pone en funcionamiento el juego."
        while not self.quit_flag:
            time = self.clock.tick(60)

            # Eventos de Salida
            for e in event.get():
                # detecta eventos
                self.scene.eventos(e)
                if e.type == QUIT:
                    self.quit_flag = True
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        self.quit_flag = True

            # actualiza la escena
            self.scene.actualizar()

            # dibuja la pantalla
            self.scene.en_escena()
            display.update()

    def change_scene(self, scene):
        "Alterna la escena actual."
        self.scene = scene
        self.quit_flag = False
