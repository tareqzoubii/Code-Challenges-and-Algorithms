# Write your test here
import pytest
from challenge03 import Tree

tree=Tree()

def test_first():
    tree.root = tree.sortedArrayToBST([-10,-3,0,5,9])
    expected = [0,-3,9,-10,5]
    actual = tree.BFS()
    assert actual == expected

def test_second():
    tree.root = tree.sortedArrayToBST([1,3])
    expected = [3,1]
    actual = tree.BFS()
    assert actual == expected

