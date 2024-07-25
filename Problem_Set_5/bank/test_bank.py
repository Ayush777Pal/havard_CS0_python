from bank import value

def test_value():
    assert value("hello")== "$0"
    assert value("namaste")=="$100"
    assert value("hey")=="$20"
    assert value("ujjj@!#")=="$100"