import random
from piezas import vertices, nro_piezas, colors
from cubo import Cubo

class Pieza:
    def __init__(self):
        type_piece = random.randint(0, nro_piezas-1)
        _vertices = list(map(lambda v: map(lambda x: x/10.0, v), vertices[type_piece]))
        self.cubos = [Cubo(_vertices[i], colors[type_piece]) for i in range(0, len(_vertices), 4)]

    def move(self, x, y, z):
        map(lambda c: c.move(x, y, z), self.cubos)

    def secure_move(self, direction, cantidad, map):
        x = 0 if direction in ["up", "down"] else cantidad
        y = 0 if direction in ["left", "right"] else cantidad
        z = 0

        self.move(x, y, z)

        if map.collide(self, direction):
            self.move(-x, -y, -z)
            return False

        return True

    def rotate(self, degrees):
        map(lambda c: c.rotate(degrees), self.cubos)

    def secure_rotate(self, degrees, map):
        for i in range(4):
            self.rotate(degrees)

            if not map.collide(self, ""):
                break

    def draw(self):
        map(lambda c: c.draw(), self.cubos)

    def __getitem__(self, n):
        return self.cubos[n]