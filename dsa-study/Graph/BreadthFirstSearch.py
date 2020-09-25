from Graph import Graph

def bfs(g, source):
    visited = [False for _ in range(g.vertices)]
    result, visited = bfs_helper(g, source, visited)

    for i in range(g.vertices):
        if not visited[i]:
            resultNew, visited = bfs_helper(g, i, visited)
            result += resultNew

    return result

def bfs_helper(g, source, visited):
    result = []
    visited = [False for _ in range(g.vertices)]

    queue = [source]
    visited[source] = True

    while queue:
        vertex = queue.pop(0)
        result.append(vertex)

        temp = g.arr[vertex].head
        while temp:
            if not visited[temp.value]:
                queue.append(temp.value)
                visited[temp.value] = True
            temp = temp.next

    return result, visited

g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(2, 3)

result = bfs(g, 0)
print(result)