def check(L, V):  # L as Positional List and V as a value
    x = 0
    y = len(L)-1
    z = None
    while x < len(L):  # loop for all possible pair
        if L[x] + L[y] == V:  # check for possible pair
            if z == None:  # check if Z is none and add first pair
                z = [[L[x], L[y]]]
            else:
                z.append([L[x], L[y]])
        y -= 1
        if y == 0:
            y = len(L)-1
            x += 1
    return z
if __name__ == '__main__':
    print(check([1, 2, 3, 4, 5], 7))  # assuming a list and a value