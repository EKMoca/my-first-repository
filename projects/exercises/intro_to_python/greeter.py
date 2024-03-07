#Write a program named greeter.py that greets 'Victor' three times. 
#Your program should use a variable and not hard code the string value 
#'Victor' in each greeting.
first_name = 'Victor'
greetings = ['good morning,', 'good afternoon,', 'good evening,']
for i in greetings:
    print(i, first_name + '.')
    