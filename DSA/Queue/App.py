from Queue import Queue

Q = Queue()

Q.enqueue(5)
Q.enqueue(3)
Q.enqueue(6)
Q.enqueue(7)
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(11)
Q.enqueue(12)
Q.enqueue(22)
Q.enqueue(29)
Q.enqueue(99)

print(Q.data)

Q.dequeue()
Q.dequeue()

print(Q.data)
print(Q.first())

"""
print(Q._len())
print(Q.dequeue())
print(Q.isEmpty())
print(Q.dequeue())
print(Q.isEmpty())
print(Q.dequeue())
Q.enqueue(7)
Q.enqueue(9)
print(Q.ﬁrst())
Q.enqueue(4)
print(Q._len())
print(Q.dequeue())
"""