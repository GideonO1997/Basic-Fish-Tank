from TankItem import*

class BubblyThing(TankItem):
    def __init__(self, x, y, image_pre = "chest_open.gif", image_bubbles = "chest_bubbles.gif", image_post = "chest_closed.gif"):
        super().__init__(x, y, image = "chest_closed.gif")
        self._images = []
        self.open = image_pre
        self.active = image_bubbles
        self.closed = image_post
        self._state = None

    def take_turn(self, Tank):
        x = self._x
        new_x = x -20
        nb = self.open
        bb = self.active
        cl = self.closed
        index = self._state
        self._images = [cl, nb, bb]
        for x in self._images:
            return x
        self._turtle.setpos(new_x, 15)           
                
            
        
       
        
