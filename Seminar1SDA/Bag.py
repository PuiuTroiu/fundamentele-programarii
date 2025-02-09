from Iterator import Iterator
class Bag:
    def __init__(self):
        self.beg = []

    def add(self,element):
        self.beg.append(element)

    def afisare(self):
        print(self.beg)

    def search(self,element):
        if len(self.beg) > 0:
            for el in self.beg:
                if el == element:
                    return True
        return False
    def size(self):
        return len(self.beg)
    def nrOcurrences(self,element):
        nrOc = 0
        for el in self.beg:
            if el == element:
                nrOc += 1
        return nrOc

    def destroy(self):
        self.beg = None

    def iterator(self):
        iterator = Iterator(self)


