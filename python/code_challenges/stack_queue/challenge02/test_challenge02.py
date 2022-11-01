# Write your test here
import pytest
from challenge02 import is_Valid

def test_is_Valid():
    actual = is_Valid('(Tareq)')
    expected = True
    assert actual == expected

def test_is_Valid2():
    actual = is_Valid('(Tareq)[]')
    expected = True
    assert actual == expected

def test_is_Valid3():
    actual = is_Valid('()')
    expected = True
    assert actual == expected

def test_is_Valid4():
    actual = is_Valid('"[][][]"')
    expected = True
    assert actual == expected

def test_is_Valid5():
    actual = is_Valid('{Tareq}')
    expected = True
    assert actual == expected

def test_is_Valid6():
    actual = is_Valid('{[Zoubii()]}')
    expected = True
    assert actual == expected

def test_is_Valid7():
    actual = is_Valid('{[Zoubii()}')
    expected = False
    assert actual == expected

def test_is_Valid8():
    actual = is_Valid('{[](Tareq()}')
    expected = False
    assert actual == expected

def test_is_Valid9():
    actual = is_Valid('{[](Tareq()}')
    expected = False
    assert actual == expected

def test_is_Valid10():
    actual = is_Valid('()}')
    expected = False
    assert actual == expected