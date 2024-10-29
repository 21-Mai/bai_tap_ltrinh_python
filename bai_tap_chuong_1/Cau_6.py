class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Ngăn xếp rỗng"

    def is_empty(self):
        return len(self.items) == 0

    def print_stack(self):
        return self.items  

# Ví dụ 
stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
print(f"Nội dung ngăn xếp: {stack.print_stack()}")  