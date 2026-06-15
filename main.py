def tinh_diem_gpa(diem_so):
    if diem_so >= 8.5:
        return 3.5
    else:
        return (diem_so/10)*3.5 
    print("Điểm GPA hệ 4 là:", tinh_diem_gpa(8.5)) 