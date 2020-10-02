from Graph import Graph

def isTree(g):
    processed = hasCycle(g, 0, [False] * g.vertices)

    for p in processed:
        if not p:
            return False

    return True

def hasCycle(g, source, visited):
    whiteSet = set()
    greySet = set()
    blackSet = set()

    for i in range(g.vertices):
        whiteSet.add(i)

    for i in range(g.vertices):
        if i in whiteSet and hasCycleUntil(g, i, whiteSet, greySet, blackSet, visited):
            return visited

    return visited

def hasCycleUntil(g, vertex, whiteSet, greySet, blackSet, visited):
    whiteSet.remove(vertex)
    greySet.add(vertex)

    temp = g.arr[vertex].head
    while temp:
        if temp.value in greySet:
            return True
        if temp.value in blackSet:
            continue
        if hasCycleUntil(g, temp.value, whiteSet, greySet, blackSet, visited):
            return True
        temp = temp.next

    visited[vertex] = True
    greySet.remove(vertex)
    blackSet.add(vertex)

    return False

g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(3, 4)

print(isTree(g))