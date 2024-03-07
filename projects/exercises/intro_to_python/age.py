# Write a program named age.py that includes someone's age and then 
# calculates and reports the future age 10, 20, 30, and 40 years from now. 

current_age = 22
years_from_now = [10, 20, 30, 40]
print('You are', current_age, 'years old.')
for i in years_from_now:
    print('In', i, 'years, you will be ', i + current_age, 'years old.')
#You are 22 years old.
#In 10 years, you will be 32 years old.
age = 35
print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')