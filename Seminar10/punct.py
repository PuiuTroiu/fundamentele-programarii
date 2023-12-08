import math
class Punct:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    #def __sub__(self, other):
        #return Punct(self.x-other.x,self.y-other.y)

    def __sub__(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __str__(self):
        return f'X = {self.x}, Y = {self.y}'

class Cerc:
    def __init__(self,raza,centru):
        self.raza = raza
        self.centru = centru

    def arie(self):
        return math.pi * self.raza ** 2

    def __str__(self):
        # return f'Aria = {self.arie()}, Raza = {self.raza}, X_centru = {self.centru.x}, Y_centru = {self.centru.y}'
        return f'Aria = {self.arie()}, Raza = {self.raza}, {self.centru}'

    def __sub__(self, other):
        c = Cerc(self.raza - other.raza, self.centru - other.centru) # gresit
        c = Cerc(self.raza - other.raza, Punct(self.centru.x - other.centru.x,self.centru.y - other.centru.y)) #pt ca sub din clasa
        return c

def move(c1,c2):
    while not(c1.centru - c2.centru <= c1.raza + c2.raza):
        c1.centru.x += 1

def main():
    p1 = Punct(1,2)
    p2 = Punct(3,5)
    p3 = p1 - p2
    # print(p3.x,p3.y)
    c1 = Cerc(5,p1)
    print(c1)

    c2 = Cerc(7,Punct(100,2))
    # print(c1.arie(),c1.raza,c1.centru.x,c1.centru.y)
    move(c1,c2)
    print(c1)

    c3 = c1 - c2
    print(c3)

main()