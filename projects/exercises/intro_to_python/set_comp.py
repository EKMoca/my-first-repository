# { expression for element in iterable if condition }
set_comp = { number + 1 for number in range(1,11,2) }
print(set_comp)

# this is a generator expression
# add tuple constructor to create tuple object from iterable
squares = ( number + 1 for number in range(1, 6) )
print(squares)

# No Tuple, Range, String comprehensions. they're immutable.

# comprehensions don't build results all at once :
# result = empty_collection               # [], {}, set()
# for item in collection:
#     result.append(item)