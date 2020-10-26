from TankItem import *
import random

class Toy(TankItem):
    def __init__(self, x, y, max_ticks = 15, image = "toy.gif"):
        super().__init__(x, y, image = "toy.gif")
        self._maxticks = max_ticks
        self._current = 0
        self._dx = 10
        self._dy = 10
    def take_turn(self, Tank):
        w = Tank.get_width()
        h = Tank.get_height()
        if self._current < self._maxticks:
            self._x += self._dx
            #print(str(self._x) + " incrementing the x")
            if self._x > w:
                #print(str(self._x) + " x is too big")
                self._x = w
                #print(str(self._x) + " x is now equal to " + str(w))
                self._dx *= -1
                #print(str(self._dx) + " dx is now doing its work and chanign the x")
                self._x += self._dx
                
            if self._x < 0:
                #print(str(self._x) + " x is too small")
                self._x = 0
                #print(str(self._x) + " x now equal to zero")
                self._dx *= -1
                #print(str(self._dx) + " dx is now doing its work and chanign the x")
                
            self._y += self._dy
            #print(str(self._y) + " incrementing the y")
            if self._y > h: 
                self._y = h
                #print(str(self._y) + " y is now equal to " + str(h))
                self._dy *= -1
                #print str(self._y) + "dy is doing its work")
        
            if self._y < 0:   
                self._y = 0 
                self._dy *= -1
            self._turtle.goto(self._x, self._y)

        
        
        





            

        
