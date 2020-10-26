import random, turtle
from Fish import *
from BubblyThing import *
from Toy import *
class Tank:
    def __init__(self, w = None, h = None):
        #Setting the vairables
        self._turtle = turtle.Turtle()
        self._turtle.speed(0)
        self._screen = turtle.Screen()
        self._width = w
        self._height = h

        #Setting the drawing screen
        WIDTH = self._width
        HEIGHT = self._height
        self._screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
        self._screen.bgcolor("light blue")
        self._screen.title("Fish Tank")
        self._turtle.hideturtle()

        #Registering Shapes
        self._screen.addshape("chest_bubbles.gif")
        self._screen.addshape("chest_closed.gif")
        self._screen.addshape("chest_open.gif")
        self._screen.addshape("fish_left.gif")
        self._screen.addshape("fish_right.gif")
        self._screen.addshape("toy.gif")
        

        #Creating the random x and ycoordinates and also Creating and setting the list of tank items
        fish = Fish((random.randint(0, self._width)), (random.randint(0, self._height)))
        fish2 = Fish((random.randint(0, self._width)), (random.randint(0, self._height)))
        fish3 = Fish((random.randint(0, self._width)), (random.randint(0, self._height)))
        fish4 = Fish((random.randint(0, self._width)), (random.randint(0, self._height)))
        fish5 = Fish((random.randint(0, self._width)), (random.randint(0, self._height)))
        bubble = BubblyThing((random.randint(0, self._width)), (random.randint(0, self._height)))
        #bubble2 = BubblyThing((random.randint(0, self._width)), (random.randint(0, self._height)))
        toy = Toy((random.randint(0, self._width)), (random.randint(0, self._height)))
        self._items = [toy, fish, fish2, fish3, fish4, fish5]

        
    def get_width(self):
        return self._width
        
    def get_height(self):
        return self._height
        
    def draw(self):
        print("no")
        
    def run(self):
        items = self._items
        tk = Tank(self._width, self._height)
        for i in range (250):
            for x in (items):
                x.take_turn(tk)
            for x in self._items:
                x.draw()
                    
                

                         


    
def main():
    t = Tank(600, 800)
    t.run()

main()









    
