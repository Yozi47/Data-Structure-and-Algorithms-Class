# R-4.6
def Harmonic_number(n):
    if n == 1:  # Check if the number is one or not
        return 1
    else:
        return 1/n + Harmonic_number(n-1)  # returns the harmonic number for n number
number = int(input("Enter a number to obtain harmonic number: "))
print(Harmonic_number(number))

'''
"Description"
From the above code we first check the input number is 1
if it is 1 then it return 1 as harmonic number
if its not 1 then there is a recursion of function Harmonic_number() by passing
n-1 then the result is added with 1/n
finally, return the final computed harmonic number
'''
