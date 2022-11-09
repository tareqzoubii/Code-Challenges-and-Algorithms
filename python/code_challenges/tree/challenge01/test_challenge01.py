# Write your test here
import pytest
from challenge01 import trees


def test_one():
    tree=trees([-1],[-1])
    actual=tree.value
    expected=-1
    assert actual==expected


def test_two():
    list=[]
    tree=trees([3,9,1,2,20,15,7],[1,9,2,3,15,20,7])
    list.append(tree.value)
    list.append(tree.left.value)
    list.append(tree.right.value)
    list.append(tree.left.left.value)
    list.append(tree.left.right.value)
    list.append(tree.right.left.value)
    list.append(tree.right.right.value)
    actual=list
    expected=[3,9,20,1,2,15,7]

    assert actual==expected