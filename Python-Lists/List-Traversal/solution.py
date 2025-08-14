"""
Problem: List Traversal
Link: https://www.geeksforgeeks.org/problems/list-traversal

Description:
Given a list, traverse and print all its elements.

Example:
Input: [1, 2, 3, 4]
Output: 1 2 3 4

Approach:
- Iterate through the list using a loop and print each element.
"""

# Function to traverse and print elements of a list
def traverse_list(lst):
    for item in lst:
        print(item, end=" ")
