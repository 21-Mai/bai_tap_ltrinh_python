class Ngay:
    def __init__(self, ngay=1, thang=1, nam=2000):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def hien_thi(self):
        print(f"{self.ngay}/{self.thang}/{self.nam}")

class NhanVien:
    def __init__(self, ho_ten, ngay_sinh, ngay_vao_cong_ty):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.ngay_vao_cong_ty = ngay_vao_cong_ty

    def hien_thi_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print("Ngày sinh: ", end="")
        self.ngay_sinh.hien_thi()
        print("Ngày vào công ty: ", end="")
        self.ngay_vao_cong_ty.hien_thi()

# Ví dụ
ngay_sinh = Ngay(28, 8, 2005)
ngay_vao_cong_ty = Ngay(10, 1, 2025)
nhan_vien = NhanVien("Phung Thi Mai", ngay_sinh, ngay_vao_cong_ty)
nhan_vien.hien_thi_thong_tin()
