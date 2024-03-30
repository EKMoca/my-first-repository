# The following code causes an infinite loop
# (a loop that never stops iterating). Why?
''' counter = 0

while counter < 5:
    print(counter) '''
    
# the "counter" object stays less than 5. Therefore, the while loop has
# no reason to stop iterating.

# Modify the age.py program you wrote in 
# Exercise 3 of the Input/Output chapter. 
# The updated code should use a for loop 
# to display the future ages.


'''current_age = int(input('How old are you? '))
print(f'You are {current_age} years old.')
print()

for future in range(10, 50, 10):
    print(f'In future yeras, you will be ' 
    f'{current_age + future} years old.')
    
    
my_list1 = [6, 3, 0, 11, 20, 4, 17]
index = 0

while index < len(my_list1):
    print(my_list[index])
    index += 1
    
 for number in my_list1:
    print(number) 
    
index = 0
while index < len(my_list1):
    even_number = my_list1[index]
    
    if even_number % 2 == 0:
        print(even_number)
    index += 1
    
    
    
my_list2 = [6, 3, 0, 11, 20, 4, 17]

for number in my_list2:
    if number % 2 != 0:
        print(number)'''
    



# Print all of the even numbers in the following list of nested lists. 
# Don't use any while loops.
'''nested_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]


ind = 0
for numb in nested_list:
    for evens in numb:
        if evens  % 2 == 0:
            print(evens)
            
            
my_lisp = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

od_ev_list = []
for numerical in my_lisp:
    if numerical % 2 == 0:
        od_ev_list.append('even')
    else:
        od_ev_list.append('odd')
print(od_ev_list)'''


# Write a find_integers function that returns 
# a list of all the integers from my_tuple:
'''my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
            
def find_integers():
    integers = []
    for nums in my_tuple:
        if type(nums) == int:
            integers.append(nums)
    print(integers)
find_integers()'''

# integers = find_integers(my_tuple)
# print(integers)                    # [1, 3, -4]




# Write a comprehension that creates a dict object whose keys are strings 
# and whose values are the length of the corresponding key. 
# Only keys with odd lengths should be in the dict. 
# Use the set given by my_set as the source of strings.

'''my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

char_length = { name: len(name) 
                for name in my_set 
                if len(name) % 2 != 0 
}
print(char_length)'''



# Write a function that computes and returns the factorial of a number 
# by using a for or while loop. The factorial of a positive integer n, 
# signified by n!, is defined as the product of 
# all integers between 1 and n, inclusive:

'''def mul_list(list) :
     
    # Multiply elements one by one
    product = 1
    for i in list:
         product = product * i
    return product
n = int(input('Enter your factorial, cuh: '))    
factorial = list(range(1, (n + 1)))
    
print(mul_list(factorial))'''



# The following code uses the randrange function from Python's random library to 
# obtain and print a random integer within a given range. Using a while loop, 
# it keeps running until it finds a random number that matches the 
# last number in the range. Refactor the code so it doesn't 
# require two different invocations of randrange.


import random
highest = int(input('Enter range here: '))


for number in range(highest):
    number = random.randrange(highest + 1)
    print(number)
    if number == (highest):
        break
    


# Print all of the even numbers in the following list of nested lists.
# This time, don't use any for loops.

'''my_odds = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

my_evens = []
indy = 0
evendex = 0
while indy < len(my_odds):
    my_evens = (my_odds[indy])
    if my_evens[evendex] % 2 == 0:
        print(evendex)
    evendex += 1
    indy += 1'''
    