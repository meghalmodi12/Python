from Stack import Stack

def ReverseFile(filename):
    stack = Stack()
    lines = open(filename)

    for line in lines:
        stack.push(line.rstrip("\n"))
    lines.close()

    newLine = open(filename, 'w')
    while not stack.isEmpty():
        newLine.write(stack.pop() + '\n')
    newLine.close()

if __name__ == "__main__":
    filePath = "Sample.txt"
    ReverseFile(filePath)