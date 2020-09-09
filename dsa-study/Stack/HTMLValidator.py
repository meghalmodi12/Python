from Stack import Stack

def HTMLValidator(raw):
    stack = Stack()
    start = raw.find('<')

    while start != -1:
        end = raw.find('>', start + 1)
        if end == -1:
            return False
        tag = raw[start + 1 : end]

        if tag[0] != "/":
            stack.push(tag)
        else:
            if stack.isEmpty():
                return False
            if stack.pop() != tag[1:]:
                return False
        start = raw.find('<', end + 1)
    return stack.isEmpty()

if __name__ == "__main__":
    raw = "<body> <center> <h1> The Little Boat </h1> </center> <p> The storm tossed the little boat like a cheap sneaker in an old washing machine. The three drunken fishermen were used to such treatment, of course, but not the tree salesman, who even as a stowaway now felt that he had overpaid for the voyage. </p> <ol> <li> Will the salesman die? </li> <li> What color is the boat? </li> <li> And what about Naomi? </li> </ol> </body>"
    result = HTMLValidator(raw)
    print(result)