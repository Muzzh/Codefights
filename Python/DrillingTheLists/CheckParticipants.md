You're organizing murder mystery games for your coworkers, and came up with a lot of ideas for various groups of participants. The ith 0-based game can be played only if there are at least i people registered for it. Game number 0 is a beta that you will try out with your friends, so there's no need for participants.

You're expecting a full house, since a lot of participants signed up already. Not too many, unfortunately: looks like some games can't be played, because too few people registered for them. Given the list of participants, your task is to return the list of games for which too few people signed up.

Example

For participants = [0, 1, 1, 5, 4, 8], the output should be
checkParticipants(participants) = [2].

For the game number 2 (0-based) 2 people are required, but only one person has registered.

Input/Output

[time limit] 4000ms (py)
[input] array.integer participants

The ith element of the array contains the number of coworkers signed up for the ith game.

Guaranteed constraints:
1 ≤ participants.length ≤ 100,
0 ≤ participants[i] ≤ 150.

[output] array.integer

A sorted array of games for which too few people signed up.
