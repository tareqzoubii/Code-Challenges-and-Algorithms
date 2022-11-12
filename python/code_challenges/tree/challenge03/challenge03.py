# Write here the code challenge solution
class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.right = right
        self.left = left

class Tree:  
    def __init__(self):
        self.queue = []
        self.root = None
    
    def sortedArrayToBST(self, nums):
        return self.makeBST(nums, 0, len(nums))
        
    def makeBST(self, nums, start, end):
        if start >= end: return None
        return Node(
            value = nums[ (start + end) // 2 ],
            left = self.makeBST(nums, start, (start + end) // 2),
            right = self.makeBST(nums, 1 + ((start+end) // 2), end)
        )
    
    def BFS(self):
        '''
        this function to print nodes
        '''
        tree=[]
        if not self.root:
            return 'Empty tree'
        node= self.root
        self.queue.append(node)
        while self.queue:
            node= self.queue.pop(0)
            tree.append(node.value)
            if node.left != None:
                self.queue.append(node.left)
            if node.right != None:
                self.queue.append(node.right)
        return tree