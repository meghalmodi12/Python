# The following code will ask user to enter data and will try to convert them to integer

print("First python program")

total = 0
count = 0

while True:
    line = input('Enter data here: ')
    if line:
        try:
            number = int(line)
        except ValueError as err:
            print('Error')
            print(err)
            continue
        total = total + number
        count = count + 1
    else:
        break
if count:
    print('Total is ', total, '.')
