cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Điện năng:", dien_nang_kwh, type(dien_nang_kwh))
print("Chi phí:", chi_phi, type(chi_phi))