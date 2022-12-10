# Write here the code challenge solution
class Tree:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def Target(root, x):
    """
    this function is to return boolean true if the tree include two elements with sum of specific number
    """
    values = []

    def Two_Sum_BST(node):
        if not node:
            return False
        y = x - node.value
        if y in values:
            return True
        else:
            values.append(node.value)
        return Two_Sum_BST(node.left) or Two_Sum_BST(node.right)

    return Two_Sum_BST(root)