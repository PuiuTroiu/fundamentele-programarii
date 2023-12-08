from logik.logicaPHF import Logica
from ui.consola import Console

def main():

    Meniu = Console()
    Logica1 = Logica()

    decizie = 9

    Meniu.intro()
    dic = {0:"Egal", 1:"Ai castigat", 2:"Ai pierdut"}
    scor = 0
    while scor != 2 or scor != -2:
        inputJ = int(input(Meniu.functionality()))

        Logica1.setter_jucator(inputJ)
        Logica1.setter_calculator()

        scor += Logica1.adaugare_scor(Logica1.get_juc_nr(),Logica1.get_calc_nr())

        Meniu.calc_choise(Logica1.getter_calculator())
        Meniu.user_choise(Logica1.getter_jucator())

        if scor == 2:
            Meniu.win()
            decizie = int(input())
        if scor == -2:
            Meniu.lose()
            decizie = int(input())
        #print(scor)
        if scor == -1:
            print("Computer 1 <--> User 0")
        elif scor == 0:
            print("Computer 0 <--> User 0")
        elif scor == 1:
            print("Computer 0 <--> User 1")

        if decizie == 10:
            Meniu.mesaj_iesire()
            break
        # else:
        #     Logica1.setter_jucator(None)
        #     Logica1.set_calc_runda_noua()

main()