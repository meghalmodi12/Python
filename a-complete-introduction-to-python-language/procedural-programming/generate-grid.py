import random

def get_int(msg, minimum, default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < minimum:
                print("must be >= ", minimum)
            else:
                return i
        except ValueError as err:
            print(err)

def generate_grid(rows, columns, minimum, maximum):
    row = 0
    while row < rows:
        line = ""
        column = 0
        while column < columns:
            i = random.randint(minimum, maximum)
            s = str(i)
            while len(s) < 5:
                s = " " + s
            line += s
            column += 1
        print(line)
        row += 1

rows = get_int("Row : ", 1, None)
columns = get_int("Column : ", 1, None)
minimum = get_int("Minimum (Or Enter for 0) : ", -10000, 0)

default = 1000
if minimum < default:
    default = 2 * minimum

maximum = get_int("Maximum (Or Enter for " + str(default) + ") : ", minimum, default)

generate_grid(rows, columns, minimum, maximum)