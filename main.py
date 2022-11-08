
import math

def main ():
    
    # two arbitrary points
    you = vector(0,   0)
    tgt = vector(0,  -1)
    
    # compass
    cps = compass(you, tgt)
    
    
    # bearing angle / direction
    print( cps.bearing_deg() )


class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class compass ():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def bearing_deg(self):
        rad = self.bearing()
        return rad * (180.0 / math.pi)
    
    def bearing(self):
        x, y = self.slope(self.a, self.b)
        print(x, y)
        if x > 0:
            if y >= 0: return ((-1.0 * math.atan(y/x)) + (2.0 * math.pi))
            if y <  0: return (-1.0 * math.atan(y/x))
        elif x < 0: 
            if y >= 0: return ((-1.0 * math.atan(y/x)) + math.pi)
            if y <  0: return ((-1.0 * math.atan(y/x)) + math.pi)
        else: # x == 0:
            if y >  0: return (3.0 * math.pi )/2.0
            if y <  0: return (1.0* math.pi)/2.0
            if y == 0: return math.atan(math.pi/2.0)
            

    def slope (self, a, b):
        return (a.x - b.x), (a.y - b.y)    
    
main()
    
