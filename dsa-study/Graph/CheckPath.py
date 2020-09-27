from Graph import Graph

def checkPath(g, source, destination):
    processed = [False] * g.vertices
    stack = [source]

    while stack:
        vertex = stack.pop()
        processed[vertex] = True

        temp = g.arr[vertex].head
        while temp:
            if temp.value == destination:
                return True
            if not processed[temp.value]:
                stack.append(temp.value)
                processed[temp.value] = True
            temp = temp.next

    return False

g1 = Graph(9)
g1.addEdge(0, 2)
g1.addEdge(0, 5)
g1.addEdge(2, 3)
g1.addEdge(2, 4)
g1.addEdge(5, 3)
g1.addEdge(5, 6)
g1.addEdge(3, 6)
g1.addEdge(6, 7)
g1.addEdge(6, 8)
g1.addEdge(6, 4)
g1.addEdge(7, 8)

print(checkPath(g1, 0, 7))

g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(1, 3)
g2.addEdge(2, 3)

print(checkPath(g2, 3, 0))
