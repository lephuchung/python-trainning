# Ép kiểu sang số
# Khi dùng ha input để nhập vào từ bàn phím
# python sẽ tự gán đó là giá trị string
# Để khắc phục ta làm như sau

# Cách 1: ép trực tiếp (int sẽ ép sang số nguyên, float ép sang số thực)
num1 = int(input("Nhập vào số thứ nhất: "))
num2 = int(input("Nhập vào số thứ hai: "))
sum1 = num1 + num2
print('check sum:', sum1)

# Cách 2: ép trong phép cộng
num3 = input('Nhập cao số thứ 3: ')
num4 = input('Nhập vào số thứ 4: ')
sum2 = float(num3) + float(num4)
print('check sum2:', sum2)