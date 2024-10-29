class TamGiac:
    def __init__(self, canh1, canh2, canh3):
        self.canh1 = canh1
        self.canh2 = canh2
        self.canh3 = canh3

    def chu_vi(self):
        return self.canh1 + self.canh2 + self.canh3

    def dien_tich(self):
        
        nua_cv = self.chu_vi() / 2
        import math
        return math.sqrt(nua_cv * (nua_cv - self.canh1) * (nua_cv - self.canh2) * (nua_cv - self.canh3))

class TamGiacVuong(TamGiac):
    def __init__(self, canh_goc_vuong1, canh_goc_vuong2):
        canh_huyen = (canh_goc_vuong1**2 + canh_goc_vuong2**2) ** 0.5
        super().__init__(canh_goc_vuong1, canh_goc_vuong2, canh_huyen)

# Ví dụ
tam_giac = TamGiac(3, 4, 5)
tam_giac_vuong = TamGiacVuong(3, 4)
print(tam_giac.chu_vi())  
print(tam_giac_vuong.dien_tich())  


