student_names = ['Noris', 'Nora', 'Le', 'Hung', 'Le']
math_scores = [10, 6, 9, 8, 6]

print(student_names)
student_names2 = student_names.copy() # Copy danh sach
student_names3 = student_names.copy() # Copy danh sach
student_names.append('Haha') # Them 1 phan tu vao cuoi
student_names.append('Hihi') # Them 1 phan tu vao cuoi
student_names2.insert(1,'Norisy') # Them phan tu Norisy danh sach voi index bang 1
print(student_names.index('Le')) # Tim index cua phan tu co gia tri Le
# Tim phan tu khong co trong danh sach se xay ra loi
print(student_names.count('Le')) # Dem so phan tu co gia tri la Le
student_names.sort() # Sap xep theo alphabet
student_names.reverse() # Dao nguoc
student_names.remove('Le') # Xoa phan tu dau tien tim thay
student_names.pop() # Xoa phan tu cuoi cung cua mang
student_names3.clear() # Xoa toan bo danh sach
print(student_names)
print(student_names2)
print(student_names3)
student_names.extend(student_names2) # Noi danh sach 2 vao danh sach 1
print(student_names)