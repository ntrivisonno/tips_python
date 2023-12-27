# example of OOP - Object Orientated Program

'''
object:

circule:
- atributes: centre, radious, color
- methods: draw, move, delete
'''

class Circule:

    # Constructor: it is call when someone creates a new circule, the assigments creates its atributes
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        

    # This method use the atributes to draw the circule
    def draw(self, canvas):
        rad = self.radius
        x1 = self.center[0] - rad
        y1 = self.center[1] - rad
        x2 = self.center[0] + rad
        y2 = self.center[1] + rad
        canvas.create_oval(x1,y1,x2,y2, fill='green')

    def move(self, x, y):
        self.center = [x,y]
