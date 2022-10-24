# Write here the code challenge solution
class Node:
    """
    node class that will hold the pointers
    """
    def __init__(self, val):
        self.val = val
        self.next = None


class Linked_list:
    count=0
    def __init__(self):
        self.head=None
        self.count = 0
       
        
    def append(self, val):
        """
        inside the append function i will create another node
        """
        new_node = Node(val)
        
        if self.count == 0:
            self.head = new_node
            
        else: 
            same = self.head
            while same.next != None:
                same= same.next
            same.next = new_node
        
        self.count += 1
    
    def select_node(self, val):
        """
        this function for selecting a nodes 
        """
        current=self.head

        while current.val != val:
            current=current.next
        return current
    
    def change(self):
        """
        will add the node values to list
        """
        arr=[]
        
        current=self.head
    
        while current.next != None:

            arr.append(current.val)
            current=current.next
        
        arr.append(current.val)
        
        return arr
    
    # def remove_the_node(self,node):
    #     """
    #     will remove the selected node
    #     """
    #     node.value=node.next.value
    #     node.next=node.next.next
   
def remove_the_node(node):
        """
        will remove the selected node
        """
        node.val=node.next.val
        node.next=node.next.next

if __name__=="__main__":
    pass