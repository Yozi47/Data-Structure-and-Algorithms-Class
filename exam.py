# Problem 3

def fibonacci1(n):
    if n <= 1:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)


def fibonacci2(n):
    if n <= 1:
        return n, 0   # with the understanding that the sequence is indexed at 1
    else:
        a, b = fibonacci2(n - 1)
        return a+b, a


from matplotlib import pyplot as build
import time
# Lets take 7 different number for n which is multiple of 5
collect_time_1 = []
collect_time_2 = []
for i in range(5,36,5):
    time1_start = time.time()
    fibonacci1(i)
    time1_end = time.time()
    time1 = time1_end - time1_start
    collect_time_1.append(time1)

    time2_start = time.time()
    fibonacci2(i)
    time2_end = time.time()
    time2 = time2_end - time2_start
    collect_time_2.append(time2)

print("Data obtained for first fibonacci", collect_time_1)
print("Data obtained for second fibonacci", collect_time_2)
build.hist(collect_time_1, 100, facecolor="red")
build.hist(collect_time_2, 100, facecolor="green")
build.show()

# Problem 4
def check(a,b,c):
    if eval('a'+'+'+'b'+'=='+'c'):
        print(a, '+', b,'=',c)
    if eval('a'+'+'+'c'+'=='+'b'):
        print(a, "+", c,"=", b)
    # if eval('a'=='b'+'c'):
    #     print(a, '=', b, '+', c)
    # if eval('a'-'b'=='c'):
    #     print(a, '-', b, '=', c)
    # if eval('a'-'c'=='b'):
    #     print(a, "-", c, "=", b)
    # if eval('a'=='b'-'c'):
    #     print(a, '=', b, '-', c)
    # if eval('a'*'b'=='c'):
    #     print(a, '*', b, '=', c)
    # if eval('a'*'c'=='b'):
    #     print(a, "*", c, "=", b)
    # if eval('a'=='b'*'c'):
    #     print(a, '=', b, '*', c)
    # if eval('a'/'b'=='c'):
    #     print(a, '/', b, '=', c)
    # if eval('a'/'c'=='b'):
    #     print(a, "/", c, "=", b)
    # if eval('a'=='b'/'c'):
    #     print(a, '=', b, '/', c)

a= int(input("Enter first number: "))
b = int(input("Enter second number"))
c = int(input("Enter third number"))
check(a,b,c)