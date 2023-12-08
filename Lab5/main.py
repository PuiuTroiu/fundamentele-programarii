import string
import turtle
import repository.functii_litere
from repository.comenzi import *
from repository.instructiuni_utilizator import Instructiuni

instructiuni_utilizator = Instructiuni()

litere = {}
alfabet = string.ascii_uppercase  # Obține toate literele mari din alfabet

for litera in alfabet:
    functie_nume = f"{litera}char"
    litere[litera] = functie_nume

litere['?'] = 'intrebarechar'
litere['!'] = 'exclamarechar'
litere['.'] = 'punctchar'
litere[' '] = 'spatiuchar'

print(litere)





def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Afisare Text")

    pen = turtle.Pen()
    pen.color("orange")
    pen.width(3)

    decizie = -1
    while decizie != 0:
        decizie = int(input("Pentru desenare cuvant apasati 1, pentru creare apasati 2, pentru afisare semn apasati 3, pentru exit apasati 0:\n"))
        if decizie == 1:
            pen.clear()
            word = input("Please type in a word: ")
            word = word.upper()
            startx = -300
            starty = 0
            pen.penup()
            pen.goto(startx, starty)

            for char in word:
                functie_nume = litere.get(char)
                if functie_nume:
                    functie = getattr(repository.functii_litere, functie_nume)
                    startx, starty = functie(pen, startx, starty)
        elif decizie == 2:
            pen.hideturtle()
            pen.clear()
            print(
                '''
            W - stiloul se deplasează cu 10 pixeli înainte
            S - stiloul se mișcă cu 10 pixeli înapoi
            D - stiloul se rotește cu 45 de grade spre dreapta
            A - stiloul se rotește cu 45 de grade spre stânga
            F - ridică stiloul în sus (desenul se oprește)
            G - pune din nou stiloul jos (desenul continuă)
                '''
            )
            # instr = input("Introduceti instructiuni (folositi doar literele de comanda):")
            # while True:
            # if instructiuni_utilizator.checkedInstructiuni(instr) == True:
            # instructiuni_utilizator.nume_cheie(nume,instr)
            nume = input("Introduceti numele simbolului nou: ")
            f = open('cmd.txt','a')
            f.write(f"{nume}:")
            cmdAll(screen)
            # print(Instructiuni.lista_instr)
                # else:
                #     print("Acest caracter exista deja, introduceti alt set de instructiuni")
                #     instr = input("Introduceti instructiuni (folositi doar literele de comanda):")
            #############################################################################################
            # nume = input("introuceti numele simbolului, puteti alege din: ")
            # print(instructiuni_utilizator.lista_instr)
            # valoare = instructiuni_utilizator.get_val_cheie(nume)
            # print(valoare)
            #cmdAll(screen)

        elif decizie == 0:
            print("Exiting...")

    turtle.done()
    return 0

main()



