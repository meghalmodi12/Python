from Graph import Graph

def shortestPath(g, a, b):
    visited = [False] * g.vertices
    distance = [0] * g.vertices
    queue = [a]

    while queue:
        currentNode = queue.pop(0)
        visited[currentNode] = True

        temp = g.arr[currentNode].head
        while temp:
            if not visited[temp.value]:
                queue.append(temp.value)
                visited[temp.value] = True
                distance[temp.value] = distance[currentNode] + 1
                if temp.value == b:
                    return distance[b]
            temp = temp.next

    return -1

g = Graph(7)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(4, 5)
g.addEdge(2, 5)
g.addEdge(5, 6)
g.addEdge(3, 6)

print(shortestPath(g, 1, 5))