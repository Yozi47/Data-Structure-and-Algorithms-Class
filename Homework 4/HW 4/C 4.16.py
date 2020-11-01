# C-4.16
def reverse(string, position=0):
    if position == len(string)-1:  # Checking if the string has 1 character only
        return string[position]
    else:
        return reverse(string, position + 1) + string[position]
'''recurse the reverse function and obtain 1 character from string in different position
and add towards the end and return the obtained string'''

string = input("Give a word to reverse: ")
print(reverse(string))
