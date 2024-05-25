from Repo.student_repo import Studentrepo
class Controler:
    def __init__(self,repo: Studentrepo):
        self.repo = repo

    def sort_students(self):
        return sorted(self.repo.studenti)

    def filer_by_street(self,street):
        return [student for student in self.repo.studenti if student.adresa.street == street]