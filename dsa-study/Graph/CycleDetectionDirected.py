from Graph import Graph

def hasCycle(g):
    whiteSet = set()
    greySet = set()
    blackSet = set()
    parentMap = {}

    # Initially put all vertices in White set
    for i in range(g.vertices):
        whiteSet.add(i)

    for i in range(g.vertices):
        parentMap[i] = None
        if i in whiteSet and hasCycleUntil(g, i, whiteSet, greySet, blackSet, parentMap):
            return True

    return False

def hasCycleUntil(g, vertex, whiteSet, greySet, blackSet, parentMap):
    # Visiting the vertex, move it from white to grey
    whiteSet.remove(vertex)
    greySet.add(vertex)

    # Visiting adjacent vertices
    temp = g.arr[vertex].head
    while temp:
        # Update parent map
        parentMap[temp.value] = vertex

        # Check if vertex is in grey set, means cycle detected
        if temp.value in greySet:
            printCycle(vertex, temp.value, parentMap)
            return True

        # Check if vertex is in black set, means it is already done
        if temp.value in blackSet:
            continue

        # Traverse this vertex
        if hasCycleUntil(g, temp.value, whiteSet, greySet, blackSet, parentMap):
            return True

        temp = temp.next

    # If here means cycle was not found for this vertex
    # Move vertex from grey set to black set
    greySet.remove(vertex)
    blackSet.add(vertex)
    return False

def printCycle(vertex, startPoint, parentMap):
    print(parentMap)


g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(3, 0)
g.addEdge(3, 4)

result = hasCycle(g)
print(result)
