import turtle

class TankItem:    
    def __init__(self, x , y , image):
        self._x = x
        self._y = y
        self._image = image
        self._turtle = turtle.Turtle()
        self._turtle.hideturtle()
        self._turtle.penup()


        
        
    def take_turn(self):
        print("Error: Code 1")
    
    def change_look(self, new_look):
        self._image = new_look
        self._turtle.shape(new_look)

        
    def draw(self):
        self._turtle.shape(self._image)

        self._turtle.showturtle()
        

