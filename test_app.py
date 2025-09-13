# from app import add

# def test_add():
#     assert add(2, 3) == 5

from app import add, subtract, multiply

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 3) == -3

def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-2, 5) == -10