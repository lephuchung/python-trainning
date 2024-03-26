first_name = 'Noris'
last_name = 'Nora'
full_name = first_name + ' '+ last_name
print(full_name)
print(full_name.upper())
print(full_name.lower())
print(full_name.islower())
print(full_name.lower().islower())
print(full_name[2]) # Trả về phần tử ở vị trí thứ 2
print(full_name.index('r')) # Trả về vị tris chữ r đầu tiên
print(full_name.index(last_name)) # Trả về vị trí của chữ Nora đầu tiên
print(full_name.replace('Noris', last_name))
