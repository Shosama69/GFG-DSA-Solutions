"""
Problem: remove-duplicate-elements-from-sorted-array
Link: https://www.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/

Description:
You are given a sorted array arr[] containing positive integers.
Your task is to remove all duplicate elements from this array such that each element appears only once.
Return an array containing these distinct elements in the same order as they appeared.

Input: arr[] = [2, 2, 2, 2, 2]
Output: [2]

Approach:
We can use the two pointer approach to keep track of the position of duplicate elements,
and replacing them if any duplicates are there
"""


class Solution:
    def removeDuplicates(self, arr):
        if not arr:
            return 0
        k = 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1]:
                arr[k] = arr[i]
                k += 1

        return arr[:k]




