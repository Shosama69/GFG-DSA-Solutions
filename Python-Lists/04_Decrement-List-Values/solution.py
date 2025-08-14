"""
Problem: Decrement List Values
Link: https://www.geeksforgeeks.org/problems/decrement-list-values/

Description:
You are given a list that contains integers. You need to decrement each element of the list by 1 and return the list.

Example:
Input: arr = [54, 43, 2, 1, 5]
Output: 53 42 1 0 4

Approach:
We can create an empty list and then using a for loop we can append all the values in the new_list while decreasing value by 1.
"""

def decrementList(arr):
    new_list=[]
    for i in arr:
        new_list.append(i-1)
        
    return new_list