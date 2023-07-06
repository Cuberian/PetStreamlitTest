import functions


def test_simple_1():
    assert 1 == 1


def test_simple_2():
    assert functions.say_hello('Никита') == 'Привет, Никита'
