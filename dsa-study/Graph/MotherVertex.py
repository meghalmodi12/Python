from Graph import Graph

def findMotherVertex(g):
    found = False
    processed = [False] * g.vertices

    for i in range(g.vertices):
        if not processed[i]:
            if dfs(g, i, [False] * g.vertices):
                return i

    return -1

def dfs(g, vertex, visited):
    stack = [vertex]
    visited[vertex] = True

    while stack:
        currentVertex = stack.pop()
        temp = g.arr[currentVertex].head

        while temp:
            if not visited[temp.value]:
                stack.append(temp.value)
                visited[temp.value] = True
            temp = temp.next

    for v in visited:
        if not v:
            return False

    return True

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(3, 0)
g.addEdge(3, 1)

print(findMotherVertex(g))