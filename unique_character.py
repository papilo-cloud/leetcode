# Given a string s, find the first non-repeating character in it and return its index. 
# If it does not exist, return -1.


# Example 1:
# Input: s = "leetcode"

# Output: 0

# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:
# Input: s = "loveleetcode"

# Output: 2

# Example 3:
# Input: s = "aabb"

# Output: -1

 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.


class Solution:
    def firstUniqChar(self, s: str) -> int:

        mpp = {}
        for i in s:
            if i in mpp:
                mpp[i] += 1
            else:
                mpp[i] = 1

        for (key, val) in mpp.items():
            if val == 1:
                return s.index(key)
        return -1