class Stack:
    def __init__(self, size):
        """Khởi tạo ngăn xếp với kích thước nhất định."""
        self.size = size  # Kích thước tối đa của ngăn xếp
        self.stack = []   # Danh sách lưu trữ các phần tử trong ngăn xếp
        self.top = -1     # Chỉ số của phần tử ở đỉnh ngăn xếp

    def push(self, value):
        """Đưa một phần tử vào đỉnh ngăn xếp."""
        if self.isFull():
            print("Ngăn xếp đã đầy. Không thể thêm phần tử.")
            return
        self.stack.append(value)  
        self.top += 1              
        print(f"Đã thêm {value} vào ngăn xếp.")

    def pop(self):
        """Lấy một phần tử ra từ đỉnh ngăn xếp."""
        if self.isEmpty():
            print("Ngăn xếp rỗng. Không thể lấy phần tử.")
            return None
        value = self.stack.pop()  
        self.top -= 1             
        print(f"Đã lấy {value} ra khỏi ngăn xếp.")
        return value

    def isEmpty(self):
        """Kiểm tra xem ngăn xếp có trống không."""
        return self.top == -1  

    def isFull(self):
        """Kiểm tra xem ngăn xếp có đầy không."""
        return self.top >= self.size - 1  

    def hien_thi(self):
        """Hiển thị nội dung ngăn xếp."""
        if self.isEmpty():
            print("Ngăn xếp rỗng.")
        else:
            print("Nội dung ngăn xếp:", self.stack)

class Stack:
    def __init__(self, size):
        """Khởi tạo ngăn xếp với kích thước nhất định."""
        self.size = size  # Kích thước tối đa của ngăn xếp
        self.stack = []   # Danh sách lưu trữ các phần tử trong ngăn xếp
        self.top = -1     # Chỉ số của phần tử ở đỉnh ngăn xếp

    def push(self, value):
        """Đưa một phần tử vào đỉnh ngăn xếp."""
        if self.isFull():
            print("Ngăn xếp đã đầy. Không thể thêm phần tử.")
            return
        self.stack.append(value)  # Thêm phần tử vào danh sách
        self.top += 1              # Cập nhật chỉ số đỉnh
        print(f"Đã thêm {value} vào ngăn xếp.")

    def pop(self):
        """Lấy một phần tử ra từ đỉnh ngăn xếp."""
        if self.isEmpty():
            print("Ngăn xếp rỗng. Không thể lấy phần tử.")
            return None
        value = self.stack.pop()  # Lấy phần tử từ đỉnh
        self.top -= 1             # Cập nhật chỉ số đỉnh
        print(f"Đã lấy {value} ra khỏi ngăn xếp.")
        return value

    def isEmpty(self):
        """Kiểm tra xem ngăn xếp có trống không."""
        return self.top == -1  # Nếu top là -1 thì ngăn xếp trống

    def isFull(self):
        """Kiểm tra xem ngăn xếp có đầy không."""
        return self.top >= self.size - 1  # Nếu top lớn hơn hoặc bằng kích thước tối đa thì ngăn xếp đầy

    def hien_thi(self):
        """Hiển thị nội dung ngăn xếp."""
        if self.isEmpty():
            print("Ngăn xếp rỗng.")
        else:
            print("Nội dung ngăn xếp:", self.stack)

# Ví dụ sử dụng ngăn xếp
stack_size = 5  # Đặt kích thước ngăn xếp là 5
stack = Stack(stack_size)

# Thêm các phần tử vào ngăn xếp
stack.push(1.5)
stack.push(2.0)
stack.push(3.5)
stack.hien_thi()  
# Lấy một phần tử ra khỏi ngăn xếp
stack.pop()
stack.hien_thi() 
# Thử thêm phần tử vào ngăn xếp
stack.push(4.5)
stack.push(5.0)
stack.push(6.7)  
stack.hien_thi()  
