from Stack import Stack

def BalanceParan(data):
    left = "([{"
    arrayStack = Stack()

    for i,d in enumerate(data):
        if d in left:
            if d == "(":
                arrayStack.push(")")
            elif d == "{":
                arrayStack.push("}")
            else:
                arrayStack.push("]")
        else:
            if arrayStack.pop() != d:
                return False

    return arrayStack.isEmpty()

if __name__ == "__main__":
    print(BalanceParan("("))
