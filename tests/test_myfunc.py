from src.my_fnc import my_funct
import pytest

def test_fnc():
    result= my_funct(12,34)
    assert result == 46

def test_more():
    result=my_funct(10,10)
    assert result == 20