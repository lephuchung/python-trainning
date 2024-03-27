# quyen W se xoa toan bo du lieu hien tai trong file dich va ghi de
# neu file dich khong ton tai, quyen W se tao file dich moi
# quyen A se ghi them nhung thong tin xuong cuoi file

phone_book = open("phone_book.txt", "w")

phone_book.write("\n Hihi - 1234567887")

phone_book.close()

phone_book = open("phone_book.txt", "a")

phone_book.write("\n Haha - 1234567888")

phone_book.close()