phone_book = open('phone.txt', "r")
# r là đọc
# w là ghi đè
# a là ghi thêm vào cuối

print(phone_book.readable()) # Kiem tra quyen doc file
# print(phone_book.read()) # Doc ca file
# print(phone_book.readline()) # Doc tung dong, con tro se chuyen den dong tiep theo
# print(phone_book.readline())

for person in phone_book:
    person = person.replace('\n', '')
    print(person)

phone_book.close()
