fruits = ['apple', 'banana', 'orange', 'grape', 'peach', 'kiwi', 'banana']

for fruit in fruits:
    if fruit == 'kiwi':
        print('Noris thich an kiwi')
    else:
        print(f'Noris khong thich an {fruit}')

for so in range (len(fruits)):
    print(f"{so+1}" + " - " + fruits[so])

for chu in 'Noris Nora':
    if(chu == ' '):
        break
    print(chu)

for i in range(10):
    print(i)