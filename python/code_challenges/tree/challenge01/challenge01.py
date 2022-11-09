# Write here the code challenge solution
class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

def trees(preorder, inorder):
    '''this function to create the tree using in-order and pre-order traversal to build the tree'''
    if len(preorder)==0 or  len(inorder)==0:
        return None
    
    root=Node(preorder[0])
    mid=inorder.index(preorder[0])
    root.left= trees(preorder[1:mid+1],inorder[:mid])
    root.right=trees(preorder[mid + 1:],inorder[mid + 1:])
    return root
























