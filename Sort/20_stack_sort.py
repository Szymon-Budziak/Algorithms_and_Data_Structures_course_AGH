# Find algorithm that sorts the stack of size n in O(log(n)) time. It is allowed to use operations
# provided only by the stack interface: push(), pop(), top(), isEmpty() and additional stacks.


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False


def sort_stack(stack):
    temporary_stack = Stack()
    while not stack.isEmpty():
        value = stack.pop()
        while not temporary_stack.isEmpty() and temporary_stack.top() > value:
            stack.push(temporary_stack.pop())
        temporary_stack.push(value)
    while not temporary_stack.isEmpty():
        stack.push(temporary_stack.pop())
    result = []
    while not stack.isEmpty():
        result.append(stack.pop())
    return result


def create_stack(T):
    stack = Stack()
    for i in range(len(T)):
        stack.push(T[i])
    return stack


T = [7, 10, 7, 87, 5, 53, 10, 15, 49, 1, 73, 14, 8, 68, 2, 32, 23, 41, 35, 98, 26]
stack = create_stack(T)
print(sort_stack(stack))
