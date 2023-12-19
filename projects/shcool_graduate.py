students = {}


def regist_student(student_name, studant_graduate):
    students[student_name] =studant_graduate


def change_student(student_name, student_graduate):
    students.pop(student_name)
    students[student_name] = student_graduate

def remove_student(student_name):
    students.pop(student_name)

def show_students():
    return students

while True:
    action = input('Enter the command: ')
    if action.upper() == 'REGIST STUDENT':
        student_name = input('Enter the student name: ')
        if student_name not in students.keys():
            student_class = input('Enter the class of student: ') + ' class'
            regist_student(student_name, student_class)
            print(students)
        else:
            print('This student alreade exist!')
    elif action.upper() == 'SHOW STUDENTS':
        print(show_students())
    elif action.upper() == 'CHANGE STUDENT':
        student_name = input('Enter the name of student which you wanna change: ')
        if student_name in students.keys():
            student_class = input('Enter the number of class in which you wanna add: ' + ' class')
            change_student(student_name, student_class)
            print(students)
        else:
            print('This student not exist!')
    elif action.upper() == 'REMOVE STUDENT':
        student_name = input('Enter the student which you wanna remove: ')
        if student_name in students.keys():
            remove_student(student_name)
            print(students)
        else:
            print('This student not exist!')
             