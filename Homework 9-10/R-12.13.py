'''
In this case when the condition left<=right is replaced with left<right
then there would be flaw as the function could not handle the condition
if left==right and the function will not decrease or increase in the value
due to which the function will continuously repeat by itself ced

if sequence S = [1, 23, 4, 4, 16, 7] is given
if we take pivot as 7 then the sorting is done and partition between the
element less than 7 on left and larger than 7 on right. while on left there
would be 1,4,4 since the condition check for 1,4,4 then the condition would
repeat in infinite loop as the 4 < 4 and there wont be increase or decrease
in the number of left and right.

As a result for S = [1, 23, 4, 4, 16, 7] there wont be any output and the
program runs infinitely.
'''