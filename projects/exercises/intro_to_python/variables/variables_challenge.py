# Assume you have $1,000.00 in the bank, and you've somehow managed to 
# find a bank that pays you 5% (this is a wish-fulfillment fantasy) 
# compounded interest every year. After one year, you will have 
# $1,050 ($1,000 times 1.05). After two years, you will have 
# $1,050 times 1.05, or $1102.50. Create a variable named balance that contains
# the amount of money you will have after 5 years, then print the result. 
# Use a single expression if you can to set balance to the correct value. 
balance = 1000
print(balance)
balance *= 1.05
print(balance)
balance *= 1.05
print(balance)
balance *= 1.05
print(balance)
balance *= 1.05
print(balance)
balance *= 1.05
print(balance)

obj = 42
obj = 'ABcd' # reassigns to a string
obj.upper() # reassigns to all uppercase
obj = obj.lower() # reassigns to all lowercase
print(len(obj)) # reassigns to length of obj
obj = list(obj) # reassigns to a list
obj.pop() # neither mutates/reassigns but removes from list
obj[2] = 'X' # mutates X in place 2 of obj list
obj.sort() # neither mutates/reassigns but sorts in ascending order.
set(obj) # reassigns to a set
obj = tuple(obj) # reassigns to a tuple

    
    
