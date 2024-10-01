# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_i = 0
        n_i = 0
       
        while h_i < len(haystack):
            if needle[n_i] == haystack[h_i]:
                found = True
                while n_i < len(needle) and ((n_i + h_i) < len(haystack)):
                    if needle[n_i] != haystack[h_i + n_i]:
                        found = False
                        break
                    n_i += 1
                if found and ((len(haystack) - h_i) >= len(needle)):
                    return h_i
                n_i = 0
            h_i += 1
        return -1