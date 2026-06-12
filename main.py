def tinh_diem_gpa_tuyen_tinh(diem_so):
    if diem_so >= 8.5:
        return 4.0
    elif diem_so < 0:
        return 0.0
    else:
        # Quy đổi tỷ lệ thẳng từ hệ 10 sang hệ 4 và lấy 2 chữ số thập phân
        gpa = (diem_so / 10) * 4
        return round(gpa, 2)