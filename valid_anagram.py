
# 242. Valid Anagram
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

# Solution 1
# Time complexity: O(n)
# Space complexity: O(k)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        seen = {}
        for s1 in s:
            if s1 not in seen:
                seen[s1] = 1
            else:
                seen[s1] += 1
        for t1 in t:
            if t1 not in seen:
                return False
            if t1 in seen:
                seen[t1] -= 1
            if seen[t1]<0:
                return False
        return True

# Solution 2
# count() uses n iteration for each iteration so it is O(n**2)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        for i in set(s):
            if s.count(i)!=t.count(i):
                return False
        return True