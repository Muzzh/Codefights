Consider a bishop, a knight and a rook on an n × m chessboard. They are said to form a triangle if each piece attacks exactly one other piece and is attacked by exactly one piece. Calculate the number of ways to choose positions of the pieces to form a triangle.

Note that the bishop attacks pieces sharing the common diagonal with it; the rook attacks in horizontal and vertical directions; and, finally, the knight attacks squares which are two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from its position.



Example

For n = 2 and m = 3, the output should be
chessTriangle(n, m) = 8.



Input/Output

[time limit] 4000ms (py)
[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 40.

[input] integer m

Guaranteed constraints:
1 ≤ m ≤ 40,
3 ≤ n · m.

[output] integer
