from Stacks import ArrayStack


def reverse(data):  # This function creates a new stack and returns a reverse list
    S = ArrayStack()  # creating a new stack S
    for i in data:  # looping each element in a list
        S.push(i)  # assigning each element in list to a new stack
    reversed_list = []  # creating a new empty list get reverse of stack
    for i in range(len(S)):  # loop the number of times in Stack S
        last_item = S.pop()  # take the last item in Stack S
        reversed_list.append(last_item)  # adding popped element in reverse_list
    return reversed_list

if __name__ == '__main__':
    list_ = [2, 3, 4]  # assuming a list
    print(reverse(list_))  # calling a reverse function and print the reverse list
