# Language I: Intution, 
# Expressions: Atoms, Basic Elements
# Identifiers, Literals, Enclosures 




# basic syntax of list comprehension
# [ expression for element in iterable if condition(optional) ]
        # expression changes orig. element = Transformation
        # if condition performed in compr. = Selection

# The following code causes an infinite loop 
# (a loop that never stops iterating). Why?
counter = 0

while counter < 5:
    print(counter)
    counter += 1
    
# counter remains less than 5. To close loop, enter a break statement at the end
# or increase counter being equal to or greater than 5.


current_age = int(input('How old are you? '))
years_later = [10, 20, 30, 40]
for decade in years_later:
        future_age = (current_age + decade)
        print(f'In {decade} years, you will be {future_age} years old.')


# Use a while loop to print the numbers in my_list, 
# one number per line. Then, do the same with a for loop.        
my_list = [6, 3, 0, 11, 20, 4, 17]
element = 0
while element < len(my_list):
        print(my_list[element])
        element += 1
        
        
for ellum in range(20):
        if ellum % 2 == 0:
                continue
        else:
                print(ellum)
 
# ternary expression, chooses between two values
# syntax value1 if condition else value2
# use right side of assignment, function call, return value


# Write a function, even_or_odd, that determines whether its argument 
# is an even or odd number. If it's even, the function should print 'even'; 
# otherwise, it should print 'odd'. Assume the argument is always an integer.

def even_or_odd():
        number = int(input('enter number: '))
        print(type(number))
        return 'odd' if number % 2 != 0 else 'even'
        
        
print(even_or_odd())

# Write a function that takes a string as an argument and 
# returns an all-caps version of the string when the string 
# is longer than 10 characters. Otherwise, it should
# return the original string. 
# Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.

def all_caps(string):
        if len(string) > 10:
                return string.upper()
        else:
                return string

print(all_caps('hello world'))
print(all_caps('goodbye'))


# Write a function that takes a single integer argument
# and prints a message that describes whether:
# the value is between 0 and 50 (inclusive)
# the value is between 51 and 100 (inclusive)
# the value is greater than 100
# the value is less than 0

