import pytest
from students import School


@pytest.fixture(name='add_student')
def fixture_add_student():
    return School("Ivanov", "Ivan", 45678, {"Math": 8, "Eng": 7, "Phis": 9, "His": 8, "Nat": 7})


class TestForPytest:
    def test_add_to_school(self, add_student):
        assert fixture_add_student.add_to_school({'Kozlov' 'Ivan': (2,
                                                           {'Math': 8, 'Eng': 9, 'Phis': 5,
                                                            'His': 9, 'Nat': 9})}) \
               == 'list of all students:' \
                  "{'Sergeev' 'Ivan': [1," \
                  " {'Math': 7, 'Eng': 7, 'Phis': 9, 'His': 8, 'Nat': 7}]," \
                  "{'Krasnyi' 'Ivan': [2," \
                  " {'Math': 8, 'Eng': 9, 'Phis': 5, 'His': 9, 'Nat': 9}]},"

    @pytest.fixture(scope="function", params=[(1, "in group 1: ['Sergeev Ivan']"),
                                              (2, "in group 2:[]")])
    def param_test(self, request):
        return request.param

    def test_group(self, add_student, param_test):
        (input_val, exp_out) = param_test
        assert add_student.show_by_group(input_val)[9] == exp_out[9]

    def test_show_by_group(self, add_student, param_test):
        (input_val, exp_out) = param_test
        assert add_student.show_by_group(input_val) == exp_out

    @pytest.mark.call_by_mark
    def test_show_students_with_5_and_6(self, add_student):
        assert add_student.show_students_with_5_and_6() == '5 and 6 have: ["Ivanov Ivan group: 1"]'

    @pytest.mark.call_by_mark
    def test_show_candidates_for_automat(self, add_student):
        assert add_student.show_candidates_for_automat() == 'pretend for auto: []'

    def test_error_type_list(self):
        with pytest.raises(AttributeError):
            School([])

    def test_error_type_tuple(self):
        with pytest.raises(AttributeError):
            School(())

    def test_error_type_group_with_no_args(self, add_student):
        with pytest.raises(TypeError):
            add_student.show_by_group()

    def test_error_type_group_with_two_args(self, add_student):
        with pytest.raises(TypeError):
            add_student.show_by_group(3)

    def test_error_type_add_to_school_no_args(self, add_student):
        with pytest.raises(TypeError):
            add_student.add_to_school()


if __name__ == '__main__':
    pytest.main()
