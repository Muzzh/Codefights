A new scoring system was introduced in your university: from now on, each test will consist of the predefined list of questions, and for the ith (1-based) question a student either gets i points, or loses p points as a penalty.

Your task is to calculate the number of points a student got for some test. Implement a function that would calculate the number of points received for the test based on the given list of answers.

Example

For answers = [true, true, false, true]and p = 2, the output should be
getPoints(answers, p) = 5.

Here's why: 1 + 2 - 2 + 4 = 5.

Input/Output

[time limit] 4000ms (py)
[input] array.boolean answers

Array of student's answers. answers[i] is true if the student answered the (i + 1)th question correctly, and false otherwise.

Guaranteed constraints:
1 ≤ answers.length ≤ 20.

[input] integer p

The number of points subtracted from the final score for each incorrect result.

Guaranteed constraints:
0 ≤ p ≤ 10.

[output] integer

The number of points the student received for the test.
