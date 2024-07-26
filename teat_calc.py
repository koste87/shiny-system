def reverse_list(lst):
    return lst[::-1]


import pytest

@pytest.fixture
def my_list():
    return [1, 2, 3, 4, 5]