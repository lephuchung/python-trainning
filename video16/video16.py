# Kieu du lieu dictioneary
# Tuong tu kieu object trong js

test = {
    # Key : Value
    1: 'haha',
    "firstName" : "Noris",
    "lastName" : "Nora"
}

print(test)
print(test[1])
print(test["firstName"])
print(test.get("null")) # Tra ve none vi khong co key nao bang null
print(test.get("firstName", "key khong ton tai")) # Phan sau la gia tri mac dinh tra ve neu key khong ton tai
print(test.get("null", "key khong ton tai"))