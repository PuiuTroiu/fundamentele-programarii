class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self,w):
        print(f"{self.name} eating {w}")


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)

def baza2(n):
    if n == 0:
        return 0
    baza2(n//2)
    print(n%2)
class Pig(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,name)
        self.age = age

    def eat(self,w):
        print(f"{self.name} eating {w}")

    def sleep(self):
        print(f"{self.name} slepping")

class Chicken(Animal):
    def __init__(self,name,color):
        Animal.__init__(self,name)
        self.color = color

class Farm:
    def __init__(self,name,city,animals=[]):
        self.name = name
        self.city = city
        self.animals = animals

    def feed_animals(self,food):
        for animal in self.animals:
            animal.eat(food)


def main():
    bob = Animal('bob')
    bob.eat('plante')
    zob = Pig('zob',2)
    zob.eat('ceva')
    zob.sleep()
    lob = Chicken('lob','black')
    lob.eat('iarba')
    f = Farm('ferma verde', 'cluj',[zob,bob,lob])
    f.feed_animals('plante')
    print(baza2(10))


main()