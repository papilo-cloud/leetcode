# Given a string s, find the length of the longest 
# substring
#  without repeating characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0

        visited = [-1] *256
        count = 0
        left = 0
        right = 0

        while right < len(s):
            if visited[ord(s[right])] != -1:
                left = max(visited[ord(s[right])] + 1, left)
            visited[ord(s[right])] = right
            count = max(count, right - left + 1)
            right += 1
        return count