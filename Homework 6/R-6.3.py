from Stacks import ArrayStack


def transfer(S, T):
    for length in range(len(S)):  # loop till the length of Stack S
        last_item = S.pop()  # pop the last item from the Stack S
        T.push(last_item)  # add the popped element from Stack S to Stack T
    return T  # returns the new Stack T

if __name__ == '__main__':
    S = ArrayStack()  # assuming a new stack S
    T = ArrayStack()  # assuming a new stack T
    for i in range(1, 5):  # adding some data in stack S
        S.push(i)
    x = transfer(S, T)  # calling and printing the new Stack
    print(x)
