# Given an array of integers temperatures represents the daily temperatures, return an 
# array answer such that answer[i] is the number of days you have to wait after the ith 
# day to get a warmer temperature. If there is no future day for which this is possible,
# keep answer[i] == 0 instead.
 

# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        stk = []
        ans = [0]*n

        for i in range(n-1, -1, -1):
            while stk and temperatures[stk[-1]] <= temperatures[i]:
                stk.pop()
            if (i < n) and stk:
                ans[i] = stk[-1] - i
            stk.append(i)
        return ans