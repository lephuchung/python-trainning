# Goi module tu file khac
import test_library
import qrcode

# Dung module trong test_library
result = test_library.roll_dice(6)
print(result)

# Dung module trong qrcode
image = qrcode.make('https://www.facebook.com/le.phuchung.25040601/')
image.save('MyFacebook.png', 'PNG')
