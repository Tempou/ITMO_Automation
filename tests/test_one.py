def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


# def test_fail():
#     assert (1, 2, 3) == (3, 2, 1)


def test_not():
    a = (1, 2, 3);
    b = (3, 2, 1)
    assert not a == b


def test_list():
    x = ['a', 'b', 'c']
    y = [1, 2, 3]
    assert not x == y
    assert x != y