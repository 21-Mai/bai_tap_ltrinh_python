class Date:
    def __init__(self, ngay=1, thang=1, nam=2000):
        """Khởi tạo ngày với giá trị mặc định."""
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def display(self):
        """In ngày ra màn hình."""
        print(f"Ngày: {self.ngay}/{self.thang}/{self.nam}")

    def is_leap_year(self):
        """Kiểm tra năm nhuận."""
        return (self.nam % 4 == 0 and self.nam % 100 != 0) or (self.nam % 400 == 0)

    def next(self):
        """Tính ngày tiếp theo."""
        days_in_month = [31, 28 + (1 if self.is_leap_year() else 0), 31, 30, 31, 30, 
                          31, 31, 30, 31, 30, 31]

        self.ngay += 1  

        if self.ngay > days_in_month[self.thang - 1]:
            self.ngay = 1
            self.thang += 1

            if self.thang > 12:
                self.thang = 1
                self.nam += 1

# Ví dụ 
date = Date(29, 9, 2024)
date.display()  

date.next()    
date.display()  
