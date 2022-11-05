# Write your test here
import pytest
from challenge01 import Tree

def test_tree():
    tree = Tree()
    assert tree.trees([6,10,17,12,9],[10,6,12,17,9]).value == 10
    assert tree.trees([6,10,17,12,9],[10,6,12,17,9]).right.value == 17
    assert tree.trees([6,10,17,12,9],[10,6,12,17,9]).left.value == 6
    assert tree.trees([6,10,17,12,9],[10,6,12,17,9]).right.right.value == 9
    assert tree.trees([6,10,17,12,9],[10,6,12,17,9]).right.left.value == 12


def test_tree2():
    tree = Tree()
    assert tree.trees([-1],[-1]).value == -1
