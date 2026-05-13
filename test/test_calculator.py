from calculator import add, sub
def test_add():
    assert add(2, 3) == 5
def test_sub():
    assert sub(10, 4) == 6
def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(-8, 2) == -4
