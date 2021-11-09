from LinkedList import LinkedList
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.arr = []

        for _ in range(vertices):
            temp = LinkedList()
            self.arr.append(temp)

    def addEdge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            vertex = self.arr[source]
            vertex.insertAtHead(destination)

    def removeEdge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            adjNodeList = self.arr[source]
            adjNodeList.delete(destination)

    def addDirectedEdge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            vertex = self.arr[source]
            vertex.insertAtHead(destination)

    def addUndirectedEdge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            self.arr[source].insertAtHead(destination)
            self.arr[destination].insertAtHead(source)

    def printGraph(self):
        for i in range(len(self.arr)):
            result = []
            vertex = i
            result.append('[' + str(vertex) + ']')
            result.append(self.arr[i].printList())
            output = " ".join(result)
            print(output)