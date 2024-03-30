#Write a program named greeter.py that greets 'Victor' three times. 
#Your program should use a variable and not hard code the string value 
#'Victor' in each greeting.
first_name = 'Victor'
greetings = ['good morning,', 'good afternoon,', 'good evening,']
for i in greetings:
    print(i, first_name + '.')
    
name = 'January Fooze'
print(f'Nice to meet you, {name}!')


import time
print(time.asctime())

print(1, 2, 3, False, {'apple', 'crackle', 'pop'}, sep='')
print('a', 'b', end='', sep=','); print('c', 'd', sep=',')