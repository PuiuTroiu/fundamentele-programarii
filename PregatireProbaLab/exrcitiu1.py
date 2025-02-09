from functools import reduce
def check_letter(underage:bool,persoana):
    if persoana[0][0] in {'A','S'}:
        if underage == True:
            if int(persoana[1]) < 18:
                return 1
            else:
                return 0
        else: return 1
    else: return 0

def count_people(underage:bool,filename:str):
    oameni = []
    f = open(filename,'r')
    linii = f.readlines()
    # for linie in linii:
    #     linie = linie.rstrip('\n')
    #     persoane = linie.split(',')
    #     oameni.append(persoane)
    oameni = list(map(lambda x: x.strip().split(','),linii))
    f.close()
    rezultate = map(lambda pers: check_letter(underage, pers), oameni)
    return sum(rezultate)


def test():
    assert count_people(True,'people.txt') == 3
    assert count_people(False,'people.txt') == 7

def main():
    test()
    print(count_people(True,'people.txt'))
main()

# Es wird erwartet, dass die Lösung map, filter oder reduce und andere mathematische
# Operationen, falls erforderlich, benützt.

# Beispiel für people.txt
#       -underage + name starts with A or S:  3
#