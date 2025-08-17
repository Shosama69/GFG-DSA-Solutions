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
I've just used sets here because sets can only have unique elements.
But there are more efficient methods of doing this.
"""


class Solution:
    def removeDuplicates(self, arr):
        no_duplicates = set(arr)
        new_list = list(no_duplicates)
        sorted_list = new_list.sort()
        return new_list




