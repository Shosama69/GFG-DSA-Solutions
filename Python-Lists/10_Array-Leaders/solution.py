"""
Problem: Array Leaders
Link: https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card&selectedLang=python3

Description:
You are given an array arr of positive integers.
Your task is to find all the leaders in the array.
An element is considered a leader if it is greater than or equal to all elements to its right.
The rightmost element is always a leader.

Example:
Input: arr = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]

Approach:
We create a max_var as the rightmost element of the array,
Since rightmost element is always the leader.
We traverse from right to left as we'll already know the right element always and compare it to the left of it.
Then simply append them to the "new" list and change the max_var to that variable aswell.
"""


class Solution:
    def leaders(self, arr):
        max_var = arr[-1]
        new = [arr[-1]]
        for i in arr[-2::-1]:
            if i >= max_var:
                new.append(i)
                max_var = i

        arr[:] = new
        return arr[::-1]