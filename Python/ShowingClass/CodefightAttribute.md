At CodeFights information about the CodeFighters is stored in the database. Anny is working on the class representation of this information, and needs to come up with a class that creates objects with the following attributes: username, _id, xp and name. She has already come up with a test object:

username: "annymaster"
_id: "1234567"
xp: "1500"
name: "anny"
The problem is, she doesn't know if this will be enough. It is possible that the server will require information about additional attributes that are not yet present in Anny's representation.

Given the attribute the server requested, return its value if it is defined, and the <attribute> attribute is not defined string otherwise.

Example

For attribute = "_id", the output should be
codefighterAttribute(attribute) = "1234567";

For attribute = "age", the output should be
codefighterAttribute(attribute) = "age attribute is not defined".

Input/Output

[time limit] 4000ms (py)
[input] string attribute

An attribute the server requested.

Guaranteed constraints:
1 ≤ attribute.length ≤ 10.

[output] string

The value of the attribute if it's defined, <attribute> attribute is not defined otherwise.
