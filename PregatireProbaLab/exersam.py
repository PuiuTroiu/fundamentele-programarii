
def factorial_2(n):
    if n == 1 or n == 0:
        return 1
    p = 1
    for i in range(1,n+1):
        p *= i
    return p * factorial_2(n-1)


def insert(l):
    for i in range(1,len(l)):
        idx = i - 1
        while l[idx] > l[idx + 1] and idx >= 0:
            l[idx],l[idx+1] = l[idx+1],l[idx]
            idx -=1
        print(l)
    return l

def cel_mai_mare_numar_clienti(l):
    val_max = max(len(x.lista_Kunde) for x in l)
    print(val_max)
    list_shop_max_Kunde = list(filter(lambda x:len(x.lista_Kunde) == val_max,l))
    return list_shop_max_Kunde
class Online_shop:
    def __init__(self,Name, lista_Kunde:None):
        self.Name = Name
        self.lista_Kunde = lista_Kunde if lista_Kunde is not None else []

    def __repr__(self):
        return f'Der Name des Online Shpes {self.Name}'

def double_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * double_factorial(n - 2) if n > 0 else 1

# Exemplu de utilizare pentru n = 3

def deserializare(l):
    rezultat = []
    for element in l:
        if type(element) is list:
            rezultat.extend(deserializare(element))
        else:
            rezultat.append(element)
    return rezultat

def gradcelsius(l):
    return list(map(lambda x: 9/5*x+32,l))


class Point():
    def __init__(self,x,y,z):
        self.x = x;
        self.y = y;
        self.z = z;
        self.Farbe = 'Blau'

    def color(self,farbe):
        self.Farbe = farbe

    def __eq__(self, other):
        return self.Farbe == other.Farbe

    def __lt__(self, other):
        return self.Farbe < other.Farbe

    def __gt__(self, other):
        return self.Farbe > other.Farbe
    def __repr__(self):
        return f'{self.Farbe}'


def main():
    pct1 = Point(1,2,3)
    pct2 = Point(1,2,3)
    pct2.color('Orange')
    pct3 = Point(1,2,3)
    pct3.color('Yello')
    pct4 = Point(1,2,3)
    pct4.color('Black')
    pct5 = Point(1,2,3)
    pct5.color('Magenta')
    l = [pct1,pct2,pct3,pct4,pct5]
    l.sort()
    print(l)
main()