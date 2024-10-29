class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
    
    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)
    
    def hien_thi_thong_tin(self):
        print(f"HCN có chiều dài {self.chieu_dai} và chiều rộng {self.chieu_rong}")
        print(f"Diện tích: {self.tinh_dien_tich()}")
        print(f"Chu vi: {self.tinh_chu_vi()}")

#VD
chieu_dai = float(input("Nhập chiều dài HCN : "))
chieu_rong = float(input("Nhập chiều rộng HCN: "))
hinh_cn = HinhChuNhat(chieu_dai, chieu_rong)
hinh_cn.hien_thi_thong_tin()