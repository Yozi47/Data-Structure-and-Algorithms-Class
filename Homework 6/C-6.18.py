from Stacks import ArrayStack


def transfer(S, T):
    for length in range(len(S)):  # loop till the length of Stack S
        last_item = S.pop()  # pop the last item from the Stack S
        T.push(last_item)  # add the popped element from Stack S to Stack T
    return T

# initiating Stacks S, T and U where T and U are temporary stacks
S = ArrayStack()
T = ArrayStack()
U = ArrayStack()
# Adding the element in the stack S
S.push(1)
S.push(2)
S.push(3)
print("Initial stack")
print(S)  # printing the initial stack
transfer(S, T)
transfer(T, U)
print("Final stack")
print(transfer(U, S))  # Printing the final reverse stack
