class DaGiac:
    def __init__(self, so_dinh):
        self.so_dinh = so_dinh

class HinhBinhHanh(DaGiac):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(4)
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong

class HinhVuong(HinhBinhHanh):
    def __init__(self, canh):
        super().__init__(canh, canh)

# Ví dụ
hinh_vuong = HinhVuong(5)
print("Chu vi hình vuông:", hinh_vuong.chu_vi())
print("Diện tích hình vuông:", hinh_vuong.dien_tich())
