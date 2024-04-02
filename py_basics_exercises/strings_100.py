'~~~~~~~~~~~~~~~~~~~~~'
# Using the following code, compare the value of name with 
# the string 'RoGeR' while ignoring the case of both strings. 
# Print true if the values are the same; print false if they aren't. 
# Next, perform a case-insensitive comparison between 
# the value of name and the string 'DAVE'.

name = 'Roger'
print(name.casefold() == 'DAVE'.casefold())

'~~~~~~~~~~~~~~~~~~~~~'
# Multiline string with triple quote characters or \n
# \t = tab, spacing       \n = newline
poem = 'A pirate I was meant to be!\nTrim the sails and roam the sea!'
print(poem)

'~~~~~~~~~~~~~~~~~~~~~'
# check whether the string char_sequence contains the character x.
char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'
# char_sequence.find('x') shows char. location in numeric order, 
# otherwise it will print '-1' for not being found
print('found' if 'x' in char_sequence else 'not here')
        

'~~~~~~~~~~~~~~~~~~~~~'
# Is Empty Exercise
# Write a function that checks whether a string is empty or not:

def empty(string):
    if string:
        return 'Is not empty'
    else:
        return 'nothing here'
        
print(empty(' '))

# given solution:
# def is_empty(s):
    # return s == ''
    # or 
# def is_empty(s):
    # return len(s) == 0
    
# more pythonic approach
# by leveraging the fact that an empty string is falsy
# return the negation of the string using the 'not' keyword
def is_empty(s):
    return not s
    # because not s and '' both return falsy value
    # not s == ''
    
print(is_empty(''))

'~~~~~~~~~~~~~~~~~~~~'
 # Write an is_empty_or_blank function to determine whether 
 # a string is either empty or consists entirely of spaces. 
 
def empty_or_blank(s):
    if not s:
        return 'empty'
    elif s.isspace():
        return 'blank'
    else:
        return 'an actual word, bro....'
        
print(empty_or_blank('wordle'))
print(empty_or_blank(''))
print(empty_or_blank(' '))

'word'.isspace() 
# Return True if there are only whitespace characters in the string 
# and there is at least one character.


# given solution
# def is_empty_or_blank(s):
#    return s.strip(' ') == ''

# def is_empty_or_blank(s):
#    return len(s.strip(' ')) == 0 

# more pythonic solution
def is_empty_or_blank(s):
    return not s.strip(' ')
# if '' or '   ', return not false == True
# not empty or blank strings return not True == False


'~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
# Write code that capitalizes the words in the string 
# 'launch school tech & talk', 
# so that you get the string 'Launch School Tech & Talk'.
print('launch school tech & talk'.title())