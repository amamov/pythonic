class Node:
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer


class Stack:
    def __init__(self):
        self.header = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def push(self, value):
        self.header = Node(value, self.header)
        self.count += 1

    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            value = self.header.value
            self.header = self.header.pointer
            self.count -= 1
            return value

    def peek(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            return self.header.value

    def show(self):
        node = self.header
        while node:
            print(node.value, end="\n")
            node = node.pointer


if __name__ == "__main__":
    pass