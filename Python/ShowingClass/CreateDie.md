Don Corletwo, local Mafia boss, asked you for a favor, and you, naturally, cannot say no. An yahtzee championship will be held soon enough, and Don needs to make sure that his player has a decent chance to win. You are assigned with the task of writing the dice interface for the game. As a Python programmer, you can use the random module to generate random numbers that will determine the result of throwing an n-sides die.

Of course, random module can get predictable results if given a proper seed value. Your task is to implement a function that, given the seed for random module and the number of sides on the die n, will return the value on the die using the following formula: int(random.random() * n) + 1.

Example

For seed = 37237 and n = 5, the output should be
createDie(seed, n) = 3.

Input/Output

[time limit] 4000ms (py)
[input] integer seed

The seed for random module.

Guaranteed constraints:
2 ≤ seed ≤ 50000.

[input] integer n

The number of sides on a die.

Guaranteed constraints:
2 ≤ n ≤ 12.

[output] integer

The number obtained by rolling the die generated as described above.
