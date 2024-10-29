class PS:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
        if not self.kiem_tra_hop_le():
            raise ValueError("Mẫu số không thể bằng 0")

    def kiem_tra_hop_le(self):
        """Kiểm tra tính hợp lệ của phân số."""
        return self.mau != 0

    def nhap_phan_so(self):
        """Nhập phân số từ người dùng."""
        self.tu = int(input("Nhập tử số: "))
        self.mau = int(input("Nhập mẫu số: "))
        if not self.kiem_tra_hop_le():
            raise ValueError("Mẫu số không thể bằng 0")

    def in_phan_so(self):
        """In phân số ra màn hình."""
        print(f"Phân số: {self.tu}/{self.mau}")

# Ví dụ sử dụng
try:
    phan_so = PS(3, 4) 
    phan_so.in_phan_so()

    phan_so.nhap_phan_so()  
    phan_so.in_phan_so()
except ValueError as e:
    print(e)
