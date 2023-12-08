# def create_student(student_as_string):
#     student = {}
#     id, name,note = student_as_string.split(" ")
#     student['id'] = id.strip()
#     student['name'] = name.strip()
#     student['note'] = int(note.strip())
#
#     return student


def create_student(id,name,note):
    student = {}
    student['id'] = id.strip()
    student['name'] = name.strip()
    student['note'] = int(note.strip())

    return student

def read_student(filename):
    students = []
    f = open(filename, 'r')
    for line in f:
        students.append(create_student(*line.split(" ")))
    return students

def best_student(students):
    max_student= students[0]
    for student in students:
        if student['note'] > max_student['note']:
            max_student = student
    return max_student

def change_name(students,id,new_name):
    for student in students:
        if student['id'] == id:
            student['name'] = new_name


def main():
    students = read_student('fisier.txt')
    bs = best_student(students)
    print(bs)
    change_name(students,"102","Mikki")
    #print(student)
main()