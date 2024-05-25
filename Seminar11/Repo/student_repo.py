import pickle
import os
class Studentrepo:
    def __init__(self):
        self.studenti = []

    def add(self,student):
        self.studenti.append(student)

    def find(self,nume):
        for student in self.studenti:
            if student.name == nume:
                return student
        return None

class Filestudentrepo(Studentrepo):
    def __init__(self,filename):
        Studentrepo.__init__(self)
        self.filename = filename
        if os.path.exists(self.filename):
            self.load()

    def add(self,student):
        super().add(student)
        self.save()
    def save(self):
        f = open(self.filename,'ab')
        pickle.dump(self.studenti,f)
        f.close()

    def load(self):
        f = open(self.filename, 'rb')
        self.studenti = pickle.load(f)
        f.close()
