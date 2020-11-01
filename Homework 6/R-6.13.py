from Queues import ArrayQueue

capacity = 8
D = ArrayQueue(capacity)  # creating a queue with capacity 8
for i in range(1, 9):  # adding 8 element in D
    D.enqueue(i)

Q = ArrayQueue(capacity)  # creating an empty Queue

# Enqueue the element to the Q that is deque from D
Q.enqueue(D.dequeue())
Q.enqueue(D.dequeue())
Q.enqueue(D.dequeue())
D.enqueue(D.dequeue())
Q.enqueue(D.dequeue())
Q.enqueue(D.first())
Q.enqueue(D.dequeue())
Q.enqueue(D.dequeue())
Q.enqueue(D.dequeue())

# printing the obtained result
print(Q)

Q.enqueue(Q.dequeue())
print(Q)