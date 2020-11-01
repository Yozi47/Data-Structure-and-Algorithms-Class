from Stacks import ArrayStack
from Queues import ArrayQueue

capacity = 8
D = ArrayQueue(capacity)  # Creating a Queue with capacity 8
for i in range(1, 9):  # adding elements in D
    D.enqueue(i)

S = ArrayStack()  # creating an empty Stack

# Adding the element in stack S using push and removing element from Queue using deque
S.push(D.dequeue())
S.push(D.dequeue())
S.push(D.dequeue())
D.enqueue(D.dequeue())
S.push(D.dequeue())
S.push(D.first())
S.push(D.dequeue())
S.push(D.dequeue())
S.push(D.dequeue())

print(S)
