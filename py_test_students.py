import pytest
from students import School


@pytest.fixture(name='create_student')
def fixture_create_student():
    return School(name={'Ivan B.A': [1, {"math": 5, "biol": 5, "geom": 5, "chem": 5, "nat": 5}]})


class BeginPytest:
    def test_school_add(self, create_student):
        assert create_student.school_add('List of all students:{"Ivan B.A": [1, {"math": 5, "biol": 5, "geom": 5, '
                                         '"chem": 5, "nat": 5} "Ivan N.E": [1, {"math": 7, "biol": 6,"geom": 9, '
                                         '"chem": '
                                         '7,"nat": 6}]}')


@pytest.fixture(scope="function", params=[(1, "In This group 1: ['Ivan B.A']"),
                                          (2, 'In This group 2: []')])
def param_test(request):
    return request.param


def test_group(create_student, param_test):
    (input_value, expected_out) = param_test
    assert create_student.check_by_group(input_value)[9] == expected_out[9]


def test_check_by_group(create_student, param_test):
    (input_value, expected_out) = param_test
    assert create_student.check_by_group(input_value) == expected_out


@pytest.mark.call_by_grade
def test_list_of_5_6(create_student):
    assert create_student.list_of_5_6() == "5 and 6 have: ['Ivan B.A group: 1']"


@pytest.mark.call_by_grade
def test_average_score(create_student):
    assert create_student.average_score() == "Students pretend for auto: []"


def test_type_list():
    with pytest.raises(AttributeError):
        School(())


def test_tuple():
    with pytest.raises(AttributeError):
        School(())


def test_group_with_no_args(create_student):
    assert pytest.raises(TypeError)


def test_group_two_args(create_student):
    with pytest.raises(TypeError):
        create_student.check_by_group(1, 2)


def test_add_with_no_args(create_student):
    with pytest.raises(TypeError):
        create_student.school_add()


if __name__ == "__main__":
    pytest.main()
