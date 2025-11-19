n = int(input("Nhập số cần kiểm tra: "))
i = 0
while i * i < n:
    i += 1
if i * i == n:
    print(n, "là số chính phương")
else:
    print(n, "không phải là số chính phương")
