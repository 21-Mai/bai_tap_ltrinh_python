class ThiSinh:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa
    
    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa
    
    def hien_thi_thong_tin(self):
        print(f"Thí sinh: {self.ho_ten}")
        print(f"Điểm Toán: {self.diem_toan}, Điểm Lý: {self.diem_ly}, Điểm Hóa: {self.diem_hoa}")
        print(f"Tổng điểm: {self.tinh_tong_diem()}")

# VD
ho_ten = input("Nhập họ tên thí sinh: ")
diem_toan = float(input("Nhập điểm Toán: "))
diem_ly = float(input("Nhập điểm Lý: "))
diem_hoa = float(input("Nhập điểm Hóa: "))
thi_sinh = ThiSinh(ho_ten, diem_toan, diem_ly, diem_hoa)
thi_sinh.hien_thi_thong_tin()