from Stack import Stack

arrayStack = Stack()

arrayStack.push(5) # contents: [5] 
arrayStack.push(3) # contents: [5, 3] 
print(arrayStack.size()) # contents: [5, 3]; outputs 2 
print(arrayStack.pop()) # contents: [5]; outputs 3 
print(arrayStack.isEmpty()) # contents: [5]; outputs False 
print(arrayStack.pop()) # contents: [ ]; outputs 5 
print(arrayStack.isEmpty()) # contents: [ ]; outputs True 
arrayStack.push(7) # contents: [7] 
arrayStack.push(9) # contents: [7, 9] 
print(arrayStack.top()) # contents: [7, 9]; outputs 9 
arrayStack.push(4) # contents: [7, 9, 4] 
print(arrayStack.size()) # contents: [7, 9, 4]; outputs 3 
print(arrayStack.pop()) # contents: [7, 9]; outputs 4 
arrayStack.push(6) # contents: [7, 9, 6]
