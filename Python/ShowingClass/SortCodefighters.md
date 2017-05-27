At CodeFights the CodeFighters can get to the top of the leaderboard by earning XP (experience points) in different modes. The leaderboard is sorted by players XP in descending order, and in case of a tie - by their ids in ascending order.

Your task is to implement an algorithm that will return the state of the weekly leaderboard given a list of codefighters.

Example

For

codefighters = [["warrior", "1", "1050"],
                ["Ninja!",  "21", "995"],
                ["recruit", "3", "995"]]
the output should be
sortCodefighters(codefighters) = ["warrior", "recruit", "Ninja!"].

Input/Output

[time limit] 4000ms (py)
[input] array.array.string codefighters

A list of CodeFighters, where each CodeFighter is given in the format [username, id, xp].
It is guaranteed that all usernames and ids are unique.

Guaranteed constraints:
0 ≤ codefighters.length ≤ 104,
codefighters[i].length = 3,
1 ≤ codefighters[i][0].length ≤ 20,
1 ≤ int(codefighters[i][1]), int(codefighters[i][2]) ≤ 104.

[output] array.string

A list of CodeFighters sorted as described above.
