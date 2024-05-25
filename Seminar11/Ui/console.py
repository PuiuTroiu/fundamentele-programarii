from Entities.address import Address
from Logik.logic import Controler
from Entities.student import Student


class Console:
    def __init__(self,controller: Controler):
        self.controller = controller

    def menu(self):
        return '''
        1 --> Add Student
        2 --> Sort Student
        3 --> Exit
        4 --> Filer by street
        '''

    def run(self):
        while True:
            print(self.menu())
            opt = int(input("Input: "))

            if opt == 1:
                nume   =   input("Insert name: ")
                strada =   input("Insert street name: ")
                numar  =   int(input("Insert street number: "))
                self.controller.repo.add(Student(nume,Address(street = strada,number = numar)))
            elif opt == 2:
                students = self.controller.sort_students()
                for student in students:
                    print(student)
            elif opt == 3:
                break
            elif opt == 4:
                street = input('Street = ')
                students = self.controller.filer_by_street(street)
                for student in students:
                    print(student)
