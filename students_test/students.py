list_of_students = {'Ivan B.A': [1, {"math": 5, "biol": 5, "geom": 5, "chem": 5, "nat": 5}],
                    'Ivan V.C': [1, {"math": 3, "biol": 10, "geom": 8, "chem": 6, "nat": 5}],
                    'Ivan N.E': [1, {"math": 7, "biol": 6, "geom": 9, "chem": 7, "nat": 6}],
                    'Ivan G.Z': [2, {"math": 8, "biol": 6, "geom": 8, "chem": 8, "nat": 7}],
                    'Ivan K.L': [2, {"math": 9, "biol": 7, "geom": 9, "chem": 7, "nat": 7}]}


class Students:

    def __init__(self, name):
        self.inf = name
        self.surname = list(name.keys())
        self.grades = list(name.values())


class School(Students):
    def __init__(self, name):
        super().__init__(name)

    def school_add(self, student_name):
        self.inf.update(student_name)
        return f'List of all students: {self.inf}'

    def list_of_5_6(self):
        grade_list = []
        for key, value in self.inf.items():
            group_value = value[0]
            dict_value = value[1]
            if all(5 <= value_1 <= 6 for key_1, value_1 in dict_value.items()):
                grade_list.extend([f'{key} group: {group_value}'])

        return f'5 and 6 have: {grade_list}'

    def check_by_group(self, group):
        stud_list = []
        if group == 1:
            for key, value in self.inf.items():
                if value[0] == 1:
                    stud_list.append(key)
        if group == 2:
            for key, value in self.inf.items():
                if value[0] == 2:
                    stud_list.append(key)
        return f'In This group {group}: {stud_list}'

    def average_score(self):
        score_list = []
        for key, value in self.inf.items():
            dict_val = value[1]
            sum_dict = sum(dict_val.values())
            aver_dict = sum_dict / len(dict_val)
            if aver_dict >= 7:
                score_list.append(key)
                score_list.append(aver_dict)
        return f'Students pretend for auto: {score_list}'


students = School(list_of_students)
print(students.surname)
print(students.check_by_group(1))
print(students.check_by_group(2))
print(students.school_add({'Ivan Z.P': [2, {'math': 10, 'biol': 9, 'geom': 8, 'chem': 9, 'nat': 9}]}))
print(students.list_of_5_6())
print(students.average_score())
