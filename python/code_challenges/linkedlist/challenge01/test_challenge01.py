# Write your test here
import pytest
from challenge01 import Node,Linked_list

def test_delete():
    first_node=Linked_list()
    
    first_node.append("3")
    
    first_node.append("8")
    
    first_node.append("14")
    
    first_node.append("1")

    node=first_node.select_node("14")
    
    first_node.remove_the_node(node)
    
    expected=["3", "8", "1"]
    
    actual=first_node.change()
    
    assert expected==actual