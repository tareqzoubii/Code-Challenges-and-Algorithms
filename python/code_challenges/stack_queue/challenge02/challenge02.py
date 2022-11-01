# Write here the code challenge solution
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, value):
        "this method to push the node to the stack"
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1
    
    def pop(self):
        "this method is to change the nod from top and return it's value"
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            return ("the stack is empty")
    
    def peek(self):
        " this method is to return the node in the top"
        if self.top:
            return self.top.value
        else:
            return("the stack is empty")
    
    def is_empty(self):
        " this method is to true or false if the stack is empty or not"
        return self.size == 0
    
    def get_size(self):
        return self.size

def is_Valid(s):
    '''
    s= string 
    to check if the parantheses is valid or not
    ''' 
    stack=Stack()

    valid_par={'(':')','{':'}','[':']'}
    
    for x in s:
        if x in valid_par.keys():
            stack.push(x)
        
        elif x in valid_par.values():
            if stack.is_empty():
                return False
            
            if valid_par[stack.pop()] != x:
                return False
    
    return stack.is_empty()