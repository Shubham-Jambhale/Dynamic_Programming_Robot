# Dynamic_Programming_Robot

# Question

A robot can only walk in one of the four directions (left, right, top, bottom). The grid it is walking
on is labeled with characters of the English alphabet. The programmers of the robot have now
constrained its motion further. It can step from a grid cell A to grid cell B, if the character on cell
A is less than the character on cell B.The ordering on the characters is the lexicographic ordering.
Write a program that computes the maximum number of steps that the robot can take starting
at any grid cell.


# Example 1

>>> max_steps([[’d’, ’b’], [’c’, ’a’]])

Output : 2

d b

c a

The robot can go from ’a’ to ’b’ and then to ’d’.

# Example 2

>>> max_steps([[’t’, ’o’, ’y’], [’c’, ’a’, ’t’], [’t’, ’o’ , ’p’]])

Output : 4

t o y

c a t

t o p

The robot can go from ‘a’ to ’o’ then to ’p’ then to ’t’ and finally to ’y’

