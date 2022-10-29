# Write your test here
import pytest
from challenge01 import MyQueue

def test_push_method():
    MyQueue1 = MyQueue()
    MyQueue1.push("T")
    MyQueue1.push("A")
    MyQueue1.push("R")
    MyQueue1.push("E")
    MyQueue1.push("Q")

    expected = "T"
    # expected = "R"

    actual = MyQueue1.peek()
    
    assert actual == expected

def test_pop_method():
    MyQueue1 = MyQueue()
    MyQueue1.push("M")
    MyQueue1.push("E")
    MyQueue1.push("S")
    MyQueue1.push("I")
    # MyQueue1.pop()
    
    # expected = "E"
    # expected = "S"
    expected = "M"

    actual = MyQueue1.pop()
    
    assert actual == expected


def test_empty_method():
    MyQueue1 = MyQueue()

    MyQueue1.push("H")
    MyQueue1.push("E")
    MyQueue1.push("L")
    MyQueue1.push("L")
    MyQueue1.push("O")
    # MyQueue1.pop()
    # MyQueue1.pop()
    # MyQueue1.pop()
    # MyQueue1.pop()
    # MyQueue1.pop()

    # expected = True
    expected = False
    
    actual = MyQueue1.is_empty()
    
    assert actual == expected


    