ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")
# Lỗi 1: SyntaxError ở dòng 7 vì lệnh print thiếu dấu ) đóng ngoặc. Đã thêm dấu ).
# Lỗi 2: TypeError ở dòng 5 vì cong_suat_w nhận từ input() là str, chưa ép sang float. Đã dùng float(input(...)).
# Lỗi 3: NameError ở dòng 7 vì viết nhầm tên biến dien_nang, đúng phải là dien_nang_kwh. Đã sửa lại tên biến.