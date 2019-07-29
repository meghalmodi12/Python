import sys

zero = ["  ***  ", " *   * ", "*     *", "*     *", "*     *", " *   * ", "  ***  "]
one = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
two = [" *** ", "*   *", "*  * ","  *  ", " *   ", "*    ", "*****"]
three = [" *** ", "*   *", "    *", "   **", "    *", "*   *", " *** "]
four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]
five = ["*****", "*    ", "*    ", "**** ", "    *", "    *", "**** "]
six = ["*****", "*    ", "*    ", "*****", "*   *", "*   *", "*****"]
seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
nine = [" ***", "*  *", "*  *", " ***", "   *", "   *", "   *",]

Digits = [zero, one, two, three, four, five, six, seven, eight, nine]

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            lineData = digit[row]
            line += lineData.replace("*", str(number)) + " "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("Usage: BigDigits.py <number>")
except ValueError as err:
    print(err , " in ",digits)
