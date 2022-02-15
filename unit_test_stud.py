import unittest
from students import School


class TestStart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("unittest")
        print('^' * 50)

    @classmethod
    def tearDownClass(cls):
        print("unittest")
        print("^" * 50)

    def setUp(self):
        self.maxDiff = None
        self.just_dict = School({'Ivan B.A': [1, {'math': 8, 'biol': 7, 'geom': 4,
                                                  'chem': 9, 'nat': 9}],
                                 'Ivan V.C': [1, {'math': 3, 'biol': 10, 'geom': 8,
                                                  'chem': 6, 'nat': 5}],
                                 'Ivan N.E': [1, {'math': 6, 'biol': 5, 'geom': 6,
                                                  'chem': 6, 'nat': 5}],
                                 'Ivan G.Z': [2, {'math': 8, 'biol': 6, 'geom': 8,
                                                  'chem': 8, 'nat': 7}],
                                 'Ivan K.L': [2, {'math': 6, 'biol': 5, 'geom': 6,
                                                  'chem': 6, 'nat': 6}]})
        self.one_stud_dict = School({'Ivan B.A': [2, {'math': 5, 'biol': 5, 'geom': 5,
                                                      'chem': 5, 'nat': 5}]})
        self.new_obj_dict = ({'Ivan N.A': [1, {'math': 8, 'biol': 7, 'geom': 4,
                                               'chem': 9, 'nat': 9, 'phys': 9}],
                              'Ivan K.I': [1, {'math': 3, 'biol': 10, 'geom': 8,
                                               'chem': 6, 'nat': 5, 'phys': 8}]})
        self.students = ("List of all students: {'Ivan B.A': [1, {'math': 8, 'biol': 7, 'geom': 4, "
                         "'chem': 9, 'nat': 9}], 'Ivan V.C': [1, {'math': 3, 'biol': 10, 'geom': 8, "
                         "'chem': 6, 'nat': 5}], 'Ivan N.E': [1, {'math': 6, 'biol': 5, 'geom': 6, "
                         "'chem': 6, 'nat': 5}], 'Ivan G.Z': [2, {'math': 8, 'biol': 6, 'geom': 8, "
                         "'chem': 8, 'nat': 7}], 'Ivan K.L': [2, {'math': 6, 'biol': 5, 'geom': 6, "
                         "'chem': 6, 'nat': 6}], 'Ivan Z.P': [2, {'math': 10, 'biol': 9, 'geom': 8, "
                         "'chem': 9, 'nat': 9}]}")

        self.students_1 = ("List of all students: {'Ivan Z.P': [2, {'math': 10, 'biol': 9, 'geom': 8, "
                           "'chem': 9, 'nat': 9}]}")

        self.students_2 = "List of students in 2nd group: 'Ivan H.J': [2, {'math': 8, 'biol': 6, 'geom': 8," \
                          "'chem': 8, 'nat': 7}]," \
                          "'Ivan Y.T': [2, {'math': 6, 'biol': 5, 'geom': 6," \
                          "'chem': 6, 'nat': 6}]}"
        self.dict = School({})

    def test_school_add(self):
        self.assertEqual(self.just_dict.school_add(
            {'Ivan Z.P': [2, {'math': 10, 'biol': 9, 'geom': 8, 'chem': 9, 'nat': 9}]}), self.students)
        self.assertEqual(self.dict.school_add(
            {'Ivan Z.P': [2, {'math': 10, 'biol': 9, 'geom': 8, 'chem': 9, 'nat': 9}]}), self.students_1)

    def test_5_and_6(self):
        self.assertEqual(self.one_stud_dict.list_of_5_6(), "5 and 6 have: ['Ivan B.A group: 2']")

    def test_average_score(self):
        self.assertEqual(self.just_dict.average_score(), "Students pretend for auto: ['Ivan B.A', 7.4,"
                                                         " 'Ivan G.Z', 7.4]")

    def test_group_number(self):
        self.assertEqual(self.just_dict.check_by_group(1),
                         "In This group 1: ['Ivan B.A', 'Ivan V.C', 'Ivan N.E']")
        self.assertEqual(self.just_dict.check_by_group(2),
                         "In This group 2: ['Ivan G.Z', 'Ivan K.L']")


if __name__ == '__main__':
    unittest.main()
