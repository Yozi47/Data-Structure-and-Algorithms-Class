# R-4.7
def string_to_digit(string):
    n = len(string)
    if n == 1:
        return ord(string[0])-48  # Obtaining ASCII value and subtracting by 48 since 48 is ASCII value of number 0
    else:
        last = ord(string[n-1])-48
        return last + 10 * string_to_digit(string[:n-1])
print("Output of string number into integer number: ", string_to_digit('134531'))
'''
"Description"
From the above code if the length of string is 1 then subtract the ASCII value of 0 which is 48
If length is not 1 then pick the last letter in string then obtain its ASCII value and subtract it by 48
then add the obtained number to the recursive string_to_digit() function and multiply the function by 10
each time the function is called until the string is empty.
Finally we get string '13531' in integer 13531 form.
'''
