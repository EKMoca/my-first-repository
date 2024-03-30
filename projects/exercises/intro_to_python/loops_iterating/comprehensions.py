# [print(foo) for foo in collection]
# ordinary for loop, preferred method


# list comprehension format
# [ expression for element in iterable if condition ]

# dictionary comprehension format
# { key: value for element in iterable if condition }

squares = [number * number for number in range(5)]


# selection example
multiples_of_6 = [ number for number in range(20)
                   if number % 6 == 0 ]
print(multiples_of_6)      # [0, 6, 12, 18]

even_sqaures = [number * number
                for number in range(10)
                if number % 2 == 0
]
print(even_sqaures)


# create a list of the names in uppercase.
cats_colors = {
    'Tess':   'brown',
    'Leo':    'orange',
    'Fluffy': 'gray',
    'Ben':    'black',
    'Kat':    'orange',
}

names = [name.upper() for name in cats_colors
         if cats_colors[name] == 'orange'
         if name[0] == 'L'
]
print(names)

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10',
    'Jack', 'Queen', 'King', 'Ace',
]

deck = [
    f'{rank} of {suit}' 
    for suit in suits 
    for rank in ranks
]

print(deck)