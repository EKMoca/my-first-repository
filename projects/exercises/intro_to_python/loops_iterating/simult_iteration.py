# emulate do/while loops:
keep_going = True
while keep_going:
    
    game = input('Play again? (y/n): ')
    if game == 'n':
        break
    
# While loop test


forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
surnames = ['Camp', 'Blake', 'Flanagan', 'Short']

index = 0
while index < len(forenames):
    if index >= len(surnames):
        break
        
    forename = forenames[index]
    surname = surnames[index]
    print(f'{forename} {surname}')
        
    index += 1
    
# better for loop, simultaneous iteration

forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
surnames = ['Camp', 'Blake', 'Flanagan', 'Short']

zipped_names = zip(forenames, surnames)

for forename, surname in zipped_names:
    print(f'{forename} {surname}')