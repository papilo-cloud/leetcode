# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


class Solution:
    
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_pref = ''
        strs.sort()
        start = strs[0]
        end = strs[-1]

        for i in range(len(min(strs))):
            if start[i] != end[i]:
                return common_pref
            common_pref += start[i]
        return common_pref
