import json


def in_one_class(stud_str):
    in_one_class_dict = {}
    for student in stud_str:
        in_one_class_dict.setdefault(student['Class'], []).append(student['Name'])

    for key, value in in_one_class_dict.items():
        print(f'Students of class {key}: ')
        for student in value:
            print(student)
        print()


def section(stud_str):
    section_dict = {}
    for student in stud_str:
        section_dict.setdefault(student['Club'], []).append(student['Name'])

    for key, value in section_dict.items():
        print(f'Students in section {key}: ')
        for student in value:
            print(student)
        print()


def search_by_gender(stud_str):
    list_of_male = []
    list_of_females = []
    for student in stud_str:
        if student['Gender'] == 'M':
            list_of_male.append({student['Name']: student['Gender']})
        else:
            list_of_females.append({student['Name']: student['Gender']})

    print('List of male students: ')
    for student in list_of_male:
        for key, value in student.items():
            print(f'Name: {key}, Gender: {value}')
    print()

    print('List of female students: ')
    for student in list_of_females:
        for key, value in student.items():
            print(f'Name: {key}, Gender: {value}')


def find_student(stud_str, query=None):
    students_list = []
    if query is None:
        query = '3a'

    for student in stud_str:
        for key, value in student.items():
            if query in value:
                students_list.append({student['Name']: student['ID'], key: value})

    if students_list:
        print(f'At your request {query} was found: ')
        print(*students_list)


def main():
    with open('students.json') as file:
        student_string = json.load(file)
        in_one_class(student_string)
        print('#' * 50)
        section(student_string)
        print('#' * 50)
        search_by_gender(student_string)
        print('#' * 50)
        find_student(student_string)
        print('#' * 50)
        find_student(student_string, 'Hayato')


if __name__ == '__main__':
    main()
