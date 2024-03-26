# Except: la except default, can duoc de cuoi cung
# Vi du ve try catch
try:
    print(text) # Xay ra loi vi text chua duoc dinh nghia
except:
    print('Co loi xay ra, lien he trung tam ho tro')

# Vi du ve phep chia
try:
    print('Thuc hien phep chia')
    num1 = int(input('Nhap tu so: '))
    num2 = int(input('Nhap mau so: '))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print('Xin nhap mau so khac khong!')
except ValueError:
    print('Du lieu dau vao phai la so nguyen, xin nhap lai!')
except:
    print('Co loi xay ra')

