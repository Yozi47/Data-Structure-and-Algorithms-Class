import sys
data = []
n = 100  # assuming n has a value of 100
d = 0
for k in range(n):  # looping for 0 to n-1
    a = len(data)
    b = sys.getsizeof(data)
    if b != d and a >= 1:  # checking condition for finding the length and size in bytes
        print("length: {0:3d}; Size in bytes: {1:4d}".format(a-1, d))
    d = b  # assigning the value of b to d
    data.append(None)