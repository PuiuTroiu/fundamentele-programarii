from math import gcd


class Frac:
    def __init__(self,numitor,numarator):
        self.numitor = numitor
        self.numarator = numarator

    def extend(self,k):
      self.numitor *= k
      self.numarator *= k

    def reduce(self,k):
        g = gcd(self.numitor,self.numarator)
        self.numitor//=g
        self.numarator//=g

