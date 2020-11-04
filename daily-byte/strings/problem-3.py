"""
This question is asked by Amazon. Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position. The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively.
Ex: Given the following strings...

"LR", return true
"URURD", return false
"RUULLDRD", return true
"""

def runRobot(path):
    position = [0, 0]

    for p in path:
        if p == 'L':
            position[0] += 1
        elif p == 'R':
            position[0] -= 1
        elif p == 'U':
            position[1] += 1
        else:
            position[1] -= 1
    
    return position == [0, 0]

print(runRobot('LR'))
print(runRobot('URURD'))
print(runRobot('RUULLDRD'))