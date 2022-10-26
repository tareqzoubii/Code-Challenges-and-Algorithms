# Write your test here
import pytest
from challenge03 import Linked_list,removeNthFromEnd

def test_removeNth():
    first_node = Linked_list()
    
    first_node.append("1")
    
    first_node.append("2")
    
    first_node.append("3")
    
    first_node.append("4")
    
    first_node.append("5")
    
    node=first_node.select_node("2")
    
    removeNthFromEnd(node, 2)
    
    array=first_node.change()
    
    expected=['1', '2', '3','5']
    
    actual=array
    
    assert expected==actual

def test_removeNth():
    first_node = Linked_list()
    
    first_node.append("1")
    
    first_node.append("2")
    
    first_node.append("3")
    
    first_node.append("4")
    
    first_node.append("5")
    
    node=first_node.select_node("1")
    
    removeNthFromEnd(node, 3)
    
    array=first_node.change()
    
    expected=['1', '2', '4','5']
    
    actual=array
    
    assert expected==actual