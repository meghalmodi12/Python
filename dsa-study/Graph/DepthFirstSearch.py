from Graph import Graph

def dfs(g, source):
    visited = [False for _ in range(g.vertices)]
    result, visited = dfs_hepler(g, source, visited)

    for i in range(g.vertices):
        if not visited[i]:
            resultNew, visited = dfs_hepler(g, i, visited)
            result += resultNew

    return result

def dfs_hepler(g, source, visited):
    result = []
    stack = [source]
    visited[source] = True

    while stack:
        vertex = stack.pop()
        result.append(vertex)

        temp = g.arr[vertex].head
        while temp:
            if not visited[temp.value]:
                stack.append(temp.value)
                visited[temp.value] = True
            temp = temp.next

    return result, visited

g = Graph(7)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(3, 6)

result = dfs(g, 1)
print(result)