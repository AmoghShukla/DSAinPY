'''
Question No. : 232
Title : Implement Queue using Stacks
Difficulty : Easy

Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Example 1:
Input : ["MyQueue","push","push","peek","pop","empty"]
[[],[1],[2],[],[],[]]

Output : [null,null,null,1,1,false]
'''

class Queue:

    def __init__(self):
        self.Queue = []
    
    def push(self, x: int) -> None:
        self.Queue.append(x)
    
    def pop(self) -> int:
        return self.Queue.pop(0)
    
    def peek(self) -> int:
        return self.Queue[0]
        

    def empty(self) -> bool:
        if not self.Queue:
            return True
        else:
            return False

queue = Queue()

queue.push(21)
queue.push(22)
print(queue.peek())  
print(queue.pop())  
print(queue.empty())
