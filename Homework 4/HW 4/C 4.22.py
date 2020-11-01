# C-4.22
def power(x,n):
    if n == 0:  # check if power is 0
        return x  # if power is 0 return the number
    else:
        powr = x
        for i in range(n-1):  # loop for n number of times which is n-1
            powr *= x  # multiplying the number by x
    return powr  # return the final value
print(power(2, 5))
