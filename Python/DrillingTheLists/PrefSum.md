There is a great technique that allows finding sums of consecutive elements in the given array extremely fast. It is based on the usage of prefix sums. Given array a, your task is to calculate all its prefix sums.

Example

For a = [1, 2, 3], the output should be
prefSum(a) = [1, 3, 6].

Here's how the prefix sums can be calculated: [1, 1 + 2, 1 + 2 + 3] = [1, 3, 6].

Input/Output

[time limit] 4000ms (py)
[input] array.integer a

Guaranteed constraints:
2 ≤ a.length ≤ 3 · 104,
-1000 ≤ a[i] ≤ 1000.

[output] array.integer
