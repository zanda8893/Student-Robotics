
class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Position(self.x+other.x,self.y+other.y)
    def __subtract__(self,other):
        return Position(self.x-other.x,self.y-other.y)
