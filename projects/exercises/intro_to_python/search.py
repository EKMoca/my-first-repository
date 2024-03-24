numbers = [3, 1, 5, 9, 2, 6, 4, 7]
found_item = -1
index = 0

while index < len(numbers):
    if numbers[index] == 5:
        found_item = index
        break

    index += 1

print(found_item)

# Emulating do/while Loops:

keep_going = True
while keep_going:
    # main loop code is here

    answer = input('Play again? (y/n) ')
    if answer == 'n':
        keep_going = False