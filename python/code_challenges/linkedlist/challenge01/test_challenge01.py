# Write your test here
import pytest
from challenge01 import Node,Linked_list,remove_the_node

def test_delete():
    first_node=Linked_list()
    
    first_node.append("3")
    
    first_node.append("8")
    
    first_node.append("14")
    
    first_node.append("1")

    node=first_node.select_node("14")
    
    remove_the_node(node)
    
    expected=["3", "8", "1"]
    
    actual=first_node.change()
    
    assert expected==actual

def test_delete():
    first_node=Linked_list()
    
    first_node.append("15")

    first_node.append("72")
    
    first_node.append("9")
    
    first_node.append("25")
    
    first_node.append("39")

    node=first_node.select_node("9")
    
    remove_the_node(node)
    
    expected=["15", "72", "25", "39"]
    
    actual=first_node.change()
    
    assert expected==actual