def even_or_odd():
    number = input('Enter your number here, Buddy: ')
    if int(number) % 2 == 0:
        print('This number is definitely EVEN, cuh.')
    else:
        print('This is odd....very odd.')
    
    

# even_or_odd()


def upper_case():
    entry = input('Enter any word: ')
    if len(entry) > 10:
        print(entry.upper(), 'IS ALL CAPS!')
    else:
        print(f'no cap, >> {entry} << is low lowww lowwwww.')
        
# upper_case()

def int_value():
    numba = int(input('gimme any numba: '))
    if numba >= 0 and numba <= 50:
        print(f'{numba} is more than 0 but less than or equal to 50, CUH.')
    elif numba >= 51 and numba <= 100:
        print(f'{numba} is between 51 and, CUH.')  
    elif numba > 100:
        print(f'{numba} is more than 100, CUH.') 
    else:
        print(f'{numba} is a negative numba, CUH.') 
        
int_value()
    