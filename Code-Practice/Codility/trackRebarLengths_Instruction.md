You are making two tracks and want them to be of

maximum length, and both tracks must be equal in length.

Now, You have a bunch of rebars that can be welded

together, the rebar cannot be cut, but not all bars are

required to be exhausted in the process.



For example, if the bars are lengths 1, 2, and 3, they can

be welded together to form a brace of length 6. (Unit is

meter.)



Returns the maximum possible length of the track, or 0 if

no track can be made.



###### Example 1:

Input: \[1,2,3,6]

Output: 6

Explanation: We have two disjoint subsets {1,2,3} and {6},

which have the same sum as 6.



###### Example 2:

Input: \[1,2,3,4,5,6]

Output: 10

Explanation: We have two disjoint subsets {2,3,5} and

{4,6}, which have the same sum as 10, and the bar which

length is 1 was left.



###### Example 3:

Input: \[1,2]

output: 0

Explanation: Unable to create track, so 0 is returned.



Hint:

0 <= rebars.length <= 140

1 <= rebars\[i] <= 1000

sum(rebars\[i]) <= 5000

