# Write a program that uses a multiply function to multiply
# two numbers and returns the result. Ask the user to enter the two numbers, 
# then output the numbers and result as a simple equation.

def multiply():
    first_number = input('Enter your first number: ')
    second_number = input('Enter your second number: ')
    multiplied_numbers = float(first_number) * float(second_number)
    print(first_number, '*', second_number, '=', multiplied_numbers)
    
multiply()

def multiple(left, right):
    return left * right

def get_number(prompt):
    entry = input(prompt)
    return float(entry)

first_number = get_number('Enter the first number: ')
second_number = get_number('Enter the second number: ')
product = multiple(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')




def multiply_numbers(num1, num2, num3): 
    result = num1 * num2 * num3 #function body, function parameters
    return result # return value

product = multiply_numbers(2, 3, 4) # function invocation

# function name = multiply_numbers
# function arguments = 2, 3, 4
# def = definition
# identifiers: multiply_numbers, num1, num2, num3, result, product