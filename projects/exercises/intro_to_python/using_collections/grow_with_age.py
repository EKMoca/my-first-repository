age = input('How old are ya, Feller? ')
print()
print (f'You are {age} years old.')
decades = [10, 20, 30, 40]

for i in decades:
    future_age = (int(age) + i)
    print(f'In {i} years, you will be {future_age} years old!!!!')