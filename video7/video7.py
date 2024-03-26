# Cac cach thay tham so vao bien
Noris_age = 20
Nora_age = 22
text1 = 'Nam nay Noris {} tuoi, Nora {} tuoi'
text2 = 'Nam nay Nora {1} tuoi, Noris {0} tuoi '

# Cach 1:
print('Nam nay Noris ' + str(Noris_age) + ' tuoi, Nora ' + str(Nora_age) + ' tuoi')

# Cach 2:
print(f'Nam nay Noris {Noris_age} tuoi, Nora {Nora_age} tuoi')

# 2 cach sau, neu {} nhieu hon gia tri truyen vao, se xay ra loi
# neu {} it hon gia tri truyen vao ham thi ok
# Cach 3: Trong text1 khong danh index, python tu lay theo thu tu
print(text1.format(Noris_age, Nora_age))

# Cach 4: Trong text2 co danh index, python tuan theo index
print(text2.format(Noris_age, Nora_age))