import pytest

from app.fruit import Fruit


@pytest.fixture
def my_fruit():
    return Fruit("apple")


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


@pytest.fixture
def username():
    return "username"


@pytest.fixture(autouse=True, scope="session")
def somethink():
    print("Session begin")
    yield
    print("Session end")


@pytest.fixture
def first_entry():
    return "a"


@pytest.fixture
def order(first_entry):
    return [first_entry]
