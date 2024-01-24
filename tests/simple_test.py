import pytest

from app.main import foo, inc


def test_answer():
    assert inc(3) == 5


class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1


def test_needsfiles(tmp_path):
    print(tmp_path)
    assert 0


list_ = [("3+5", 8), ("2+4", 6), ("6*9", 54)]


@pytest.mark.parametrize("test_input,expected", list_)
def test_eval(test_input, expected):
    assert eval(test_input) == expected  # pylint: disable=W0123


@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
class TestClass:
    def test_simple_case(self, n, expected):
        assert n + 1 == expected

    def test_weird_simple_case(self, n, expected):
        assert (n * 1) + 1 == expected


def test_string(order):
    order.append("b")

    assert order == ["a", "b"]


def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket


def test_username(username):
    assert username == "username"


def test_somethink():
    assert 2 == foo()
