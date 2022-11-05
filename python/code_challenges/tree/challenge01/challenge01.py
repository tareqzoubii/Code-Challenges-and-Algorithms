# Write here the code challenge solution
class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class Tree:
    def trees(self, inorder, preorder):
        """ 
        this function to create the tree using in-order and pre-order traversal
        """
        if not inorder or not preorder:
            return None
        if len(preorder) == 1:
            return Node(preorder[0])

        root = Node(preorder[0])
        indx = inorder.index(preorder[0])
        root.left = self.trees(preorder[1:indx + 1],inorder[:indx])
        root.right = self.trees(preorder[indx + 1:],inorder[indx + 1:])
        return root
