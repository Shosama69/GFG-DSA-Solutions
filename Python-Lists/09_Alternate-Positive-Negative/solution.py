"""
Problem: Alternate Positive Negative
Link: <Problem URL>

Description:
https://www.geeksforgeeks.org/problems/array-of-alternate-ve-and-ve-nos1401/

Example:
Input: arr[] = [9, 4, -2, -1, 5, 0, -5, -3, 2]
Output: [9, -2, 4, -1, 5, -5, 0, -3, 2]

Approach:
We create two separate lists for positive and negative numbers.
We append one by one from both the lists to a new list.
Since gfg only wants its own array modified, we do that in the end.
"""


class Solution:
    def rearrange(self, arr):
        pos = [x for x in arr if x >= 0]
        neg = [x for x in arr if x < 0]
        new = []
        i = 0
        while i < len(pos) and i < len(neg):
            new.append(pos[i])
            new.append(neg[i])
            i += 1

        new.extend(pos[i:])
        new.extend(neg[i:])

        arr[:] = new

        return arr