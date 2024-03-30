stuff = ('Hello', 'World', 'Bye', 'Now')
stuff_list = list(stuff)
stuff_list[2] = 'goodbye'
print(tuple(stuff_list))

# Identify at least 2 differences between lists and tuples. 
# Identify at least 2 ways that lists and tuples are similar.
# Tuples are immutable and more memory efficient.
# Both are ordered collections that use indexing and heterogenous.

# Why can we treat strings as sequences?
# We can treat strings as sequences because they have characters that are 
# the length of one string. Ordered and accessible with indexing.

# Write some code that converts the value of pi to a string 
# and assigns it to a variable named str_pi.

pi = 3.141592
str_pi = str(pi)
print(str_pi)

# Without running the following code, 
# identify the numbers that are included in each of the following ranges:

range(7) # 0 - 6
range(1, 6) # 1 - 5
range(3, 15, 4) # 3, 7, 11
range(3, 8, -1) # []
range(8, 3, -1) # 8 - 4

print(tuple(range(3, 17, 4)))



my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Given the above code, answer the following questions and explain your answers:

# Are the lists assigned to my_list and another_list equal?
# yes

# Are the lists assigned to my_list and another_list the same object?
# no

# Are the nested lists at index 3 of my_list and another_list equal?
# yes

# Are the nested lists at index 3 of my_list and another_list the same object?
# yes

country = { 
    'Alice':     'USA', 
    'Francois':  'Canada', 
    'Inti':      'Peru', 
    'Monika':    'Germany', 
    'Sonia':     'Uganda', 
    'Yoshitaka': 'Japan' 
}

print(country['Alice'])