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