from plates import is_valid

def test_valid():
    assert is_valid("CS50")==True
    assert is_valid("CS05")==False
    assert is_valid("OUTATIME")==False
    assert is_valid("CS50P")==False
