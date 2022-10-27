# Write here the code challenge solution
class Node :
    """
     node class that will hold the pointers
    """
    def __init__(self,val):
        self.val=val
        self.next=None


class Linked_list:
   
    def __init__(self):
        self.head = None
        self.count = 0
        
    def append(self,val):
        """
        inside the append function i will create another node
        """
        new_node = Node(val)
        if self.count == 0:
            self.head = new_node
            
        else: 
            same = self.head
            while same.next != None:
                same = same.next
            same.next = new_node
        self.count += 1
    def select_node(self,val):
        """
        this function for selecting a nodes 
        """
        current=self.head
        while current.val!=val:
            current=current.next
        return current
    def change(self):
        """
        will add the node values to list
        """
        arr=[]

        current=self.head

        while current.next!=None:
            arr.append(current.val)
            current=current.next

        arr.append(current.val)
        return arr
 

   
            
def middle_node(head):
        """
        this function is getting the nodes after the middle
        """
        current = head
        count = 1
        y = current
        arr=[]
        while y.next != None:
            y=y.next
            count += 1
        mid=count // 2
        x=0
        
        
        while x < middle:
           
            current=current.next
            x += 1
        while current != None:
            arr.append(current.val)
            current = current.next
        return arr
                       


def remove_the_node(node):
        """
        will remove the selected node 
        """
        node.val=node.next.val
        node.next=node.next.next

def find_the_indexs(head,revers_indx):
    """
    will find the node index
    """
    current = head
    count = 0
    while current != None:
        count += 1
        current = current.next
    idx = count-revers_indx
    return [idx,count]

def select_the_node(head,idx):
    """
    will select the node
    """
    current = head
    count = 0
    while current != None:
        if count == idx:
            return current
        current = current.next
        count += 1
    
def removeNthFromEnd(head, n):
        """
        will take the node and the revers the index and delete the node
        """
        length = find_the_indexs(head,n)[1]
        idx = find_the_indexs(head,n)[0]
        node_for_delete = select_the_node(head,idx)
        
        if length==1:
            return None
        idx2 = find_the_indexs(head,n+1)[0]
        previous_node = find_the_indexs(head,idx2)
        if node_for_delete.next != None:
            remove_the_node(node_for_delete)
        else :
            previous_node.next=previous_node.next.next
        return head
