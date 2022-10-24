# Write your test here
# test challenge 2
import pytest
from challenge02 import Linked_list,middle_node

def test_find_middle_node():

    first_node=Linked_list()
    
    first_node.append("1")
    
    first_node.append("2")
    
    first_node.append("3")
    
    first_node.append("4")
    
    first_node.append("5")
    
    first_node.append("6")
    
    node = first_node.select_node("1")
    
    middle = middle_node(node)
    
    expected=['4', '5', '6']
    
    actual=middle
    
    assert expected == actual

def test_find_middle_node():

    first_node=Linked_list()
    
    first_node.append("1")
    
    first_node.append("2")
    
    first_node.append("3")
    
    first_node.append("4")
    
    first_node.append("5")
    
    node = first_node.select_node("1")
    
    middle = middle_node(node)
    
    expected=['3', '4', '5']
    
    actual=middle
    
    assert expected == actual