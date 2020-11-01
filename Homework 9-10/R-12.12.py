'''
In this case when the condition left<=right is replaced with left<right
then there would be flaw as it will not include the middle element of
the given sequence where left == right.
Then it will skip the condition and the element is missed placed

a sequence S = [10, 12, 6, 5, 7]
if we give S as an sequence 0 as left and 4 as right
 we take 7 as a pivot in first case it collect 10 and 12 on the right side
and 1 and 5 on left. it moves to the next pivot on the left at 0 and 0 as left
and right and calls back the function since the left and right are equal then
it doesnot do anything instead move forward to right side and same thing as left
condition doesnot applies and skips the same happens on right as
well.

As a result it gives [6, 5, 7, 12, 10]

'''