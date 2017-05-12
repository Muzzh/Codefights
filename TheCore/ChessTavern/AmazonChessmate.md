An amazon (also known as a queen+knight compound) is an imaginary chess piece that can move like a queen or a knight (or, equivalently, like a rook, bishop, or knight). The diagram below shows all squares which the amazon attacks from e4 (circles represent knight-like moves while crosses correspond to queen-like moves).



Recently you've come across a diagram with only three pieces left on the board: a white amazon, white king and black king. It's black's move. You don't have time to determine whether the game is over or not, but you'd like to figure it out in your head. Unfortunately, the diagram is smudged and you can't see the position of the black's king, so it looks like you'll have to check them all.

Given the positions of white pieces on a standard chessboard, determine the number of possible black king's positions such that:

it's checkmate (i.e. black's king is under amazon's attack and it cannot make a valid move);
it's check (i.e. black's king is under amazon's attack but it can reach a safe square in one move);
it's stalemate (i.e. black's king is on a safe square but it cannot make a valid move);
black's king is on a safe square and it can make a valid move.
Note that two kings cannot be placed on two adjacent squares (including two diagonally adjacent ones).

Example

For king = "d3" and amazon = "e4", the output should be
amazonCheckmate(king, amazon) = [5, 21, 0, 29].



Red crosses correspond to the checkmate positions, orange pluses refer to checks and green circles denote safe squares.

For king = "a1" and amazon = "g5", the output should be
amazonCheckmate(king, amazon) = [0, 29, 1, 29].



Stalemate position is marked by a blue square.

Input/Output

[time limit] 4000ms (py)
[input] string king

Position of the white's king in the chess notation.

[input] string amazon

Position of the white's amazon in the same notation.

Guaranteed constraints:
amazon ≠ king.

[output] array.integer

Array of four integers, each equal to the number of black's king positions corresponding to a specific situation. The integers should be presented in the same order as the situations were described, i.e. 0 for checkmates, 1 for checks, etc.
