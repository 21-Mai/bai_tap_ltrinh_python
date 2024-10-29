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

    def count(self):
        return len(self.items)  # Hàm trả về số phần tử trong ngăn xếp

# Ví dụ sử dụng
stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
print(f"Số phần tử trong ngăn xếp: {stack.count()}")  # In ra số phần tử trong ngăn xếp