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

class MyQueue:
    '''
        push(int x) Pushes element x to the back of the queue.
        pop() Removes the element from the front of the queue and returns it.
        peek() Returns the element at the front of the queue.
        empty() Returns true if the queue is empty, false otherwise
    '''
    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()

    def push(self, value):
        "push method -->  Pushes element x to the back of the queue."
        while self.second_stack.top:
            self.first_stack.push(self.second_stack.pop())

        self.first_stack.push(value)

        while self.first_stack.top:
            self.second_stack.push(self.first_stack.pop())
    
    def pop(self):
        "pop() Removes the element from the front of the queue and returns it"
        if not self.second_stack:
            return self.second_stack
        else:
            return self.second_stack.pop()
        
    def peek(self):
        "Returns the element at the front of the queue"
        if not self.second_stack:
            return self.second_stack
        else:
            return self.second_stack.peek()
    
    def is_empty(self):
        "Returns true if the queue is empty, false otherwise"
        if not self.second_stack:
            return self.second_stack
        else:
            return self.second_stack.is_empty()


if __name__ == "__main__":
    pass
    # MyQueue1 = MyQueue()
    # MyQueue1.push("T")
    # MyQueue1.push("A")
    # MyQueue1.push("R")
    # MyQueue1.push("E")
    # MyQueue1.push("Q")
    # print(MyQueue1.peek())
    # print(MyQueue1.pop())
    # print(MyQueue1.peek())
    # print(MyQueue1.is_empty())