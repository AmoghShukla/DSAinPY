'''
Question No. : 225
Title : Implement Stack using Queues
Difficulty : Easy

Implement a last in first out (LIFO) stack using only two queues. 
The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Example 1:
Input : ["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output : [null, null, null, 2, 2, false]
'''

class MyStack:

    def __init__(self):
        self.Stack = []

    def push(self, x: int) -> None:
        self.Stack.append(x)

    def pop(self) -> int:
        return self.Stack.pop(-1)

    def top(self) -> int:
        return self.Stack[-1]

    def empty(self) -> bool:
        if not self.Stack:
            return True
        else:
            return False