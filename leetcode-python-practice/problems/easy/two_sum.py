"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy

Approach:
- Use a hashmap to store numbers and their indices
- For each number, calculate its complement (target - num)
- If the complement exists in the hashmap, return the pair of indices

Time Complexity: O(n)
Space Complexity: O(n)
"""

def two_sum(nums, target):
    hashmap = {}  # value: index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
