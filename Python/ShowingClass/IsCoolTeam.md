You are organizing a team of eSportsmen, and you are determined to make it cool. You are already thinking about winning the world championship: when it happens, the names of your teammates will be chanted one after another by a large audience. You believe that it will sound cool if and only if the first letter of one player's name will be the same as the last letter in the name of the player before them.

Now you are considering one particular team. Its members are definitely professional gamers, but you're not sure if all together they form a cool team. Implement a function that will check if the team is cool.

Example

For team = ["Mark", "Kelly", "Kurt", "Terk"], the output should be
isCoolTeam(team) = true.

The following team announcement will sound cool: "Mark", "Kurt", "Terk", "Kelly".

Input/Output

[time limit] 4000ms (py)
[input] array.string team

A list of team members, where each team member is given by their name (a string consisting of English characters).

Guaranteed constraints:
1 ≤ team.length ≤ 100,
1 ≤ team[i].length ≤ 20.

[output] boolean

true if the team is cool, false otherwise.
