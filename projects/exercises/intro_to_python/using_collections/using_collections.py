# Write Python code to print the seventh number of range(0, 25, 3).

coolio = list(range(0, 25, 3))

print(coolio[6])

# Use slicing to write Python code to print a 6-character 
# substring of 'Launch School' that begins with the first c.

launch = 'Launch School'

print(launch[4:10])

# Write Python code to create a new tuple from (1, 2, 3, 4, 5). 
# The new tuple should be in reverse order from the original. 
# It should also exclude the first and last members of the original. 
# The result should be the tuple (4, 3, 2).

orig = (1, 2, 3, 4, 5)
reverse_orig = tuple((reversed(orig[1:4])))

print(reverse_orig)


# Part 1: Write some code to print Bark by accessing the 
# element associated with the key Dog.
# Part 2: Write some code to print None when you try to 
# print the value associated with the non-existent key, Lizard.
# Part 3: Write some code to print <silence> when you try to 
# print the value associated with the non-existent key, Lizard.

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

print(pets['Dog'])
print(pets.get('Lizard'))
print(pets.get('Lizard', '<silence>'))
print(pets)


# Which of the following values can't 
# be used as a key in a dict object, and why?
'cat' 
(3, 1, 4, 1, 5, 9, 2)
['a', 'b'] # mutable
{'a': 1, 'b': 2} # mutable
range(5) 
{1, 4, 9, 16, 25} # mutable 
3
0.0
frozenset({1, 4, 9, 16, 25})

print('abc-def'.isalpha()) # false
print('abc_def'.isalpha()) # false
print('abc def'.isalpha()) # false
print('abc def'.isalpha() and
      'abc def'.isspace()) # false
print('abc def'.isalpha() or
      'abc def'.isspace()) # true
print('abcdef'.isalpha()) # true
print('31415'.isdigit()) # true
print('-31415'.isdigit()) # false
print('31_415'.isdigit()) # false
print('3.1415'.isdigit()) # false
print(''.isspace()) # true

# Write Python code to replace all the : characters in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
info = info.replace(':', '+')
print(info)
# info = (info.split(':'))
# print('+'.join(info))

# Explain why the code below prints different values on lines 3 and 4.

texty = "It's probably pining for the fjords!"

print(texty[21:35].rfind('f'))     # 8 putting index on the left of rfind method
                                   # returns argument between start:stop,
                                   # treating start as '0'
print(texty.rfind('f', 21, 35))    # 29 argument start and stop values on the
                                   # right of rfind method returns place in 
                                   # entire string.
                                 

# Write some code to replace the value 6 in the following nested list with 606:

stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

stuff[1][3] = 606

# Consider the following nested collection:

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

# Write one line of code to print the activities that Cocoa enjoys.
print(cats['Pete']['Cocoa']['enjoys'])

# Write some code that determines 
# and prints whether the number 3 appears inside each of these lists:

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

print(3 in numbers1, 3 in numbers2, 3 in numbers3, 3 in numbers4, 3 in numbers5)


# Without running the following code, 
# determine what each print statement should print.

cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats) # True
print('Butter' in cats) # False
print('Butter' in cats[3]) # True
print('cheddar' in cats) # False

# Assume you have the following sequences:

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

# Write some code that combines the sequences into a list of tuples. 
# Each tuple should contain one member of each sequence. 
# Print the final result so you can see all the values, 
# which should look like this:

# [('a', 'Alpha', None, 10),
# ('b', 'Bravo', True, 20),
# ('c', 'Charlie', False, 30)]

zipped_list = zip(my_str, my_list, my_tuple, my_range)
print(list(zipped_list))

# Without running the following code, what values will be printed by line 10?

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys) # 'Cat':  'Meow',
            # 'Bird': 'Tweet',
            # 'Snake': 'Sssss',