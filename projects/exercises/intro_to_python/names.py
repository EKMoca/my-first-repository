# Chapter: Collections and Iteration
# sub-chapter, Loops and Iterating

'''names = ['Chris', 'Max', 'Karis', 'Victor']  # We want to append each name, 
upper_names = []                             # in uppercase, to the initially
index = 0                                    # empty upper_names list.
# don't want to initialize these variables inside the loop; 
# they would get reset during every iteration.

print(len(names)) # *index different than total length len().

while index < len(names):
    upper_name = names[index].upper()
    upper_names.append(upper_name)
    index += 1

print(upper_names);
# ['CHRIS', 'MAX', 'KARIS', 'VICTOR']'''


# re-written with for loop:

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = [] # assign variable to an empty list, when appending 1 list
                 # to another using a for loop.

for name in names:
    if name == 'Max':  # can also do negated if conditional
        continue       # if name != 'Max':  *no continue*
    
    upper_name = name.upper()
    upper_names.append(upper_name)
    # Deleted: index += 1

print(upper_names);
# ['CHRIS', 'MAX', 'KARIS', 'VICTOR']


burger_ingredients = ['pickles', 'lettuce', 'tomato', 'beef']
upper_burgers = []

for burger in burger_ingredients:
    if burger == 'lettuce':
        continue
    
    upper_burger = burger.upper()
    upper_burgers.append(upper_burger)
    
print(upper_burgers)


# for loop essential template
'''for value in collection:
    if some_condition():
        # some code here
        if another_condition():
            # some more code here'''
            
# for value in collection:
    # if not some_condition():
        # continue

    # some code here

    # if not another_condition():
        # continue

    # some more code here