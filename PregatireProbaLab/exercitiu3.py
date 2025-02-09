from functools import reduce


def selection(l):
    for i in range(len(l)-1):
        idx = i
        for j in range(i+1,len(l)):
            if l[j] <= l[i]:
                idx = j
                l[i], l[idx] = l[idx], l[i]
    return l

class Kurs:
    def __init__(self,Title,Referent):
        self.Title = Title
        self.Referent = Referent
        self.list_student = []

    def adaugare_elev(self,elev:str):
        self.list_student.append(elev)

    def __repr__(self):
        return f'Der Kurs heisst {self.Title}, der Referent heisst {self.Referent} und hat {len(self.list_student)}'

def functie(Kursen_list):
    lista_cursuri_a = list(filter(lambda x: x.Title[0].lower() == 'a',Kursen_list))
    # nrelevi = reduce(lambda x, elevi: elevi + len(x), lista_cursuri_a, 0)
    nrelevi = sum(len(curs.list_student) for curs in lista_cursuri_a)
    print(nrelevi)

def main():
    print(selection([3,2,5,4,6,73,8,4,6,3]))
    curs1 = Kurs('Matematica','Modoi')
    curs1.adaugare_elev("stefan")
    curs1.adaugare_elev("mihai")
    curs1.adaugare_elev("andrei")
    curs1.adaugare_elev("raul")
    curs2 = Kurs('Astronomie','Sacarea')
    curs2.adaugare_elev("stef")
    curs2.adaugare_elev("miki")
    curs2.adaugare_elev("andi")
    curs2.adaugare_elev("rauleto")
    curs3 = Kurs('Asc','dragos')
    curs3.adaugare_elev("stefanel")
    curs3.adaugare_elev("mikiel")
    curs3.adaugare_elev("andiel")
    functie([curs1,curs2,curs3])
main()