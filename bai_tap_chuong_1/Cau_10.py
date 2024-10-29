class Diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def thong_tin(self):
        return f"Điểm tọa độ ({self.x}, {self.y})"

class Elip(Diem):
    def __init__(self, x, y, ban_kinh_lon, ban_kinh_nho):
        super().__init__(x, y)
        self.ban_kinh_lon = ban_kinh_lon
        self.ban_kinh_nho = ban_kinh_nho

    def dien_tich(self):
        import math
        return math.pi * self.ban_kinh_lon * self.ban_kinh_nho

# Ví dụ 
diem = Diem(0, 0)
elip = Elip(0, 0, 5, 3)
print(diem.thong_tin())  
print(elip.dien_tich())  
