"""
Problem: Repetitive Addition of Digits
Link: https://www.geeksforgeeks.org/problems/repetitive-addition-of-digits2221/

Description:
You are given a positive integer n,
you need to add all the digits of n and create a new number.
Perform this operation until the resultant number has only one digit in it.
Return the final number obtained after performing the given operation.

Example:
Input: n = 1234
Output: 1
Explanation: Step 1: 1 + 2 + 3 + 4 = 10. Step 2: 1 + 0 = 1

Approach:
We can use nested while loop to solve this in looping method.
To solve this in more mathematical way we can use n%9 method
"""


class Solution:
    def singleDigit(self, n):
        while n >= 10:
            s = 0
            while n > 0:
                s += n % 10
                n = n // 10
            n = s

        return n



