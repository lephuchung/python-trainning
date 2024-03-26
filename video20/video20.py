# Tinh luy thua
a = 2
b = 3
# a^b = 2^3 = a**b
print('check a^b: ', a**b)

def power(base_number, exponent):
    result = 1
    for i in range(exponent):
        result = result * base_number

    return result

print('check power(2,3) = 2^3 = ',power(2,3))