import random
class Logica():
    def __init__(self):
        self.matrice = \
               [[0,0,0,0],
               [0, 0, -1,1],
               [0, 1, 0, -1],
               [0, -1, 1, 0]]
        self.optiuni = [1,2,3]
        self.jucator = None
        self.computer = None

    def setter_calculator(self):
        'Se face aegerea random pentru computer'
        self.computer = random.choice(self.optiuni)
        # print(f"Alegera calculatorului este: {self.computer}")

    def set_calc_runda_noua(self):
        self.computer = None

    def setter_jucator(self,alg1):
        self.jucator = alg1

    def getter_jucator(self):
        #return self.jucator
        if self.jucator == 1:
            return "Schere"
        elif self.jucator == 2:
            return "Stein"
        elif self.jucator == 3:
            return "Papier"

    def get_calc_nr(self):
        return self.computer

    def get_juc_nr(self):
        return self.jucator

    def getter_calculator(self):
        #return self.computer
        if self.computer == 1:
            return "Schere"
        elif self.computer == 2:
            return "Stein"
        elif self.computer == 3:
            return "Papier"

    def adaugare_scor(self,a,b):
        return self.matrice[a][b]


