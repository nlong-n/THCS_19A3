tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
a, b = abs(tu), abs(mau)
while b != 0:
    a, b = b, a % b
ucln = a
tu_gon = tu // ucln
mau_gon = mau // ucln
print("Phân số tối giản là:", tu_gon, "/", mau_gon)
