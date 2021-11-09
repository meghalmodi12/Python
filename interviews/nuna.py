# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
   
# Helper function to generate parent map
def generateMap(root):
    parentMap = dict()
    
    if root is None:
        return parentMap
    
    queue = deque()
    queue.append(root)
    
    parentMap[root.val] = None
    
    while queue:
        node = queue.popleft()
        
        if node.left:
            parentMap[node.left.val] = node.val
            queue.append(node.left)
            
        if node.right:
            parentMap[node.right.val] = node.val
            queue.append(node.right)
            
    return parentMap

# Helper function to generate set of nodes that we need to keep
def getNodesToKeep(parentMap, arrNodes):
    resultSet = set()
    
    for node in arrNodes:
        # Path to root
        parent = parentMap[node]
        while parent is not None:
            resultSet.add(parent)
            parent = parentMap[parent]
            
        # Add direct sibling
        parent = parentMap[node]
        for key, val in parentMap.items():
            if val == parent:
               resultSet.add(key)
               
    return resultSet

# Helper function to check rule #2 (indirect case)
def checkSibling(targetSet, parentMap, node):
    parent = parentMap[node]
    arrSiblings = []
    
    for key, val in parentMap.items():
        if val == parent:
            arrSiblings.append(key)
            
    for s in arrSiblings:
        if s in targetSet:
            return True
        
    return False
   
# Main function that uses all other helper function to modify given tree
def pruneTree(root, arrNodes):
    if root is None:
        return root
    
    queue = deque()
    queue.append(root)
    
    parentMap = generateMap(root)
    nodesToKeep = getNodesToKeep(parentMap, arrNodes)

    while queue:
        node = queue.popleft()
        
        if node.left:
            queue.append(node.left)
            lVal = node.left.val
            if not ((lVal in arrNodes) or (lVal in nodesToKeep) or checkSibling(nodesToKeep, parentMap, lVal)):
                node.left = None
            
                
        if node.right:
            queue.append(node.right)
            rVal = node.right.val
            if not ((rVal in arrNodes) or (rVal in nodesToKeep) or checkSibling(nodesToKeep, parentMap, rVal)):
                node.right = None
                
    return root

# Helper function to print tree in level by level order 
def levelOrderTraverse(root):
        result = []
        
        if root is None:
            return result

        queue = deque()
        queue.append(root)
        
        while queue:
            tempResult = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tempResult.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            result.append(tempResult)

        return result
    
### Test ###
root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')
root.right.left = TreeNode('F')

arrSet = ['B', 'F']

result = levelOrderTraverse(pruneTree(root, arrSet))