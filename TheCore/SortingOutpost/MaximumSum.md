You are given an array of integers arr. Range sum query is defined by a pair of non-negative integers L and R (L ≤ R). An output to a range sum query on the given array is the sum of all elements of arr with indices from L to R inclusive.

Find an algorithm that given a list of range sum queries can rearrange the array arr in such a way that the total sum of all of the query outputs is maximized.

Example

For arr = [2, 1, 2] and queries = [[0, 1]], the output should be
maximumSum(arr, queries) = 4.

Input/Output

[time limit] 4000ms (py)
[input] array.integer arr

An initial array.

Guaranteed constraints:
2 ≤ arr.length ≤ 10,
1 ≤ arr[i] ≤ 10.

[input] array.array.integer queries

Array of range sum queries, each query is an array of two non-negative integers.

Guaranteed constraints:
1 ≤ queries.length ≤ 10,
0 ≤ queries[i][0] ≤ queries[i][1] < arr.length.

[output] integer

Maximum possible total sum of the given range sum query outputs.
