from Ui.console import Console
from Repo.student_repo import Studentrepo, Filestudentrepo
from Logik.logic import Controler

def main():
    print('Which repo? 1 - memory/2 - file')

    val = int(input())
    if val == 1:
        repo = Studentrepo()
    else:
        repo = Filestudentrepo('students.data')

    c = Console(Controler(repo))
    c.run()

main()