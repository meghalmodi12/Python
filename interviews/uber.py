class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def serialize(root):
    result = ''

    if root is None:
        return result

    stack = [[root, 0, '']]
    while stack:
        currNode, depth, nodeTag = stack.pop()
        result += '.' * depth + nodeTag + str(currNode.value)

        if currNode.right:
            stack.append([currNode.right, depth + 1, 'R'])

        if currNode.left:
            stack.append([currNode.left, depth + 1, 'L'])

    return result

def deserialize(s):
    if len(s) == 0:
        return None

    stack = []
    startIdx = 0
    root = None

    while startIdx < len(s):
        nodeVal, nodeTag, depth, startIdx = getSingleNodeData(s, startIdx)
        newNode = Node(int(nodeVal))

        if nodeTag == '':
            root = newNode
        else:
            currentNode = None
            if depth > stack[-1][1]:
                currentNode = stack[-1][0]
            else:
                while len(stack) > 0 and depth <= stack[-1][1]:
                    stack.pop()
                currentNode = stack[-1][0]

            if nodeTag == 'L':
                currentNode.left = newNode
            else if nodeTag == 'R':
                currentNode.right = newNode

        stack.append([newNode, depth])

    return root

def getSingleNodeData(s, start):
    depth = 0
    nodeData = ''
    nodeTag = ''

    while s[start] == '.':
        depth += 1
        start += 1

    while start < len(s) and s[start] != '.':
        nodeData += s[start]
        start += 1

    if nodeData[0] == 'L':
        nodeTag = 'L'
        nodeData = nodeData[1:]

    if nodeData[0] == 'R':
        nodeTag = 'R'
        nodeData = nodeData[1:]

    return [nodeData, nodeTag, depth, start]

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.left.left = Node(4)
root.left.left.right = Node(4)
root.left.left.left.left = Node(5)

s = serialize(root)
r = deserialize(s)

print(s)
print(serialize(r))