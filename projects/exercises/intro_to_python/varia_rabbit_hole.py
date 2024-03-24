# same object ID

numbers = [1, 2, 3]
numbers2 = numbers

print(numbers)                # [1, 2, 3]
print(numbers == numbers2)    # True
print(numbers is numbers2)    # True
print(id(numbers), id(numbers2))

test = {1, 4, 5}
test1 = {1, 4, 5}
print(test == test1) # True
print(test is test1) # False, mutable obj. 

nested_list = [[1, 2], 3, 4]

print(
    id(nested_list), 
    id(nested_list[0]), 
    id(nested_list[1]), 
    id(nested_list[2])
)


# shallow copies
import copy

orig = [[1, 2], 3, 4]
dup = copy.copy(orig)

print(orig is dup)           # False, distinct/separate objects 
print(orig == dup)           # True
orig[2] = 44
print(dup)                   # [[1, 2], 3, 4]

print(orig[0] is dup[0])     # True
orig[0][1] = 22
print(dup[0])                # [1, 22]
# shallow copy, dup points to the same inner list.


# In your own words, explain the difference between these two expressions.
my_object1 = []
my_object2 = my_object1
my_object1 == my_object2 # checks if they are equal to each other in value.

my_object1 is my_object2 # checks that they are identical and reference
# the same object.

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)
# set2, set1 share the same object.



dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])
# two identical objects aren't necessarily the same object. 
# If you assign an object associated with variable a to variable b, 
# the variables share that object. However, 
# if the value assigned to b is an entirely new object, 
# there is no sharing, even if the values are identical.

# two dicts with equal-value objects associated 
# with every key may also share those objects.



import copy

dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = copy.deepcopy(dict1) # You may modify the `???` part
            # of this line

# All of these should print False
print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])

# All of these should print True
# immutables
print(dict1['a'][0][0] is dict2['a'][0][0])
print(dict1['a'][0][1] is dict2['a'][0][1])
print(dict1['a'][1][0] is dict2['a'][1][0])
print(dict1['a'][1][1] is dict2['a'][1][1])
print(dict1['b'][0][0] is dict2['b'][0][0])
print(dict1['b'][0][1] is dict2['b'][0][1])
print(dict1['b'][1][0] is dict2['b'][1][0])
print(dict1['b'][1][1] is dict2['b'][1][1])


dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1) # You may modify the `???` part
            # of this line

print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])