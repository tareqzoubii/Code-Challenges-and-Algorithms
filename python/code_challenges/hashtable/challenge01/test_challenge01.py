# Write your test here
import pytest
from challenge01 import Target, Tree


def test_sum_bst():
    tree1 = Tree(5)
    tree1.left = Tree(1)
    tree1.left.left = Tree(1)
    tree1.left.right = Tree(4)
    tree1.right = Tree(7)
    tree1.right.right = Tree(11)
    actual = Target(tree1, 3)
    expected = False
    assert actual == expected


def test_sum_bst_tow():
    tree1 = Tree(10)
    tree1.left = Tree(5)
    tree1.left.left = Tree(4)
    tree1.left.right = Tree(8)
    tree1.right = Tree(12)
    tree1.right.right = Tree(17)
    actual = Target(tree1, 27)
    expected = True
    assert actual == expected