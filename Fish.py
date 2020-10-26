from TankItem import *


class Fish(TankItem):
    def __init__(self, x, y, image_right = "fish_right.gif", image_left = "fish_left.gif"):
        super().__init__(x, y, image ="fish_right.gif" )
        self._imageright = image_right
        self._imageleft = image_left
        self._dx = 5

    def take_turn(self, Tank):
        w = Tank.get_width()
        h = Tank.get_height()
        self._x += self._dx
        if (self._x > w):
            self._x = w
            self._dx *= -1
            self._image = self._imageleft
        elif(self._x < 0):
            self._x = 0
            self._dx *= -1
            self._image = self._imageright
        self._turtle.goto(self._x, self._y)



