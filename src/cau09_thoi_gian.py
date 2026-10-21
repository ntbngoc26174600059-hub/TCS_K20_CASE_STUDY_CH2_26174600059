from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))
# datetime: kiểu thời điểm (ngày giờ cụ thể), trừ được cho nhau.
# str: chuỗi chữ, ở đây là thời điểm đã định dạng bằng strftime để hiển thị, không tính toán thời gian được.
# timedelta: kiểu khoảng thời gian, là kết quả của phép trừ hai datetime (ở đây là 1 giờ 50 phút).