from Graph import Graph

def numOfEdges(g):
    result = 0

    for i in range(g.vertices):
        temp = g.arr[i].head
        while temp:
            result += 1
            temp = temp.next

    # Half the total sum as it is an undirected graph
    return result // 2

g = Graph(9)
g.addUndirectedEdge(0, 2)
g.addUndirectedEdge(0, 5)
g.addUndirectedEdge(2, 3)
g.addUndirectedEdge(2, 4)
g.addUndirectedEdge(5, 3)
g.addUndirectedEdge(5, 6)
g.addUndirectedEdge(3, 6)
g.addUndirectedEdge(6, 7)
g.addUndirectedEdge(6, 8)
g.addUndirectedEdge(6, 4)
g.addUndirectedEdge(7, 8)

result = numOfEdges(g)
print(result)