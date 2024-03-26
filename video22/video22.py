def translate(text):
    translation = ""
    for char in text:
        if char.lower() in 'áàảãạăắằẳẵặâầấẩẫậ':
            if char.isupper():
                translation = translation + 'A'
            else:
                translation = translation + 'a'

        elif char.lower() in 'éèẻẽẹêếềểễệ':
            if char.isupper():
                translation = translation + 'E'
            else:
                translation = translation + 'e'

        elif char.lower() in 'úùủũụưứừửữự':
            if char.isupper():
                translation = translation + 'U'
            else:
                translation = translation + 'u'

        elif char.lower() in 'íìĩịỉ':
            if char.isupper():
                translation = translation + 'I'
            else:
                translation = translation + 'i'

        elif char.lower() in 'ýỳỷỹỵ':
            if char.isupper():
                translation = translation + 'Y'
            else:
                translation = translation + 'y'

        elif char.lower() in 'óòỏõọôồốỗộổơờởớỡợ':
            if char.isupper():
                translation = translation + 'O'
            else:
                translation = translation + 'o'

        else:
            translation = translation + char

    return translation

text = input("Nhập vào chữ muốn chuyển: ")
print(translate(text))