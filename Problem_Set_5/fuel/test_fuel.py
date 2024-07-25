import pytest
from fuel import convert, gauge

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("2/1")
        convert("cat")
    
def test_convert():
    assert convert("1/4")== 25
    assert convert("4/4")== 100
    assert convert("0/4")== 0

def test_gauge():
    assert gauge(25)== 25
    assert gauge(100)=="F"
    assert gauge(0)=="E"