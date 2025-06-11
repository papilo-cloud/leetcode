from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        cost = [[0] * cols for _ in range(rows)]
        
        cost[0][0] = grid[0][0]
        
        for i in range(1, rows):
            cost[i][0] = cost[i - 1][0] + grid[i][0]
        for j in range(1, cols):
            cost[0][j] = cost[0][j - 1] + grid[0][j]
        
        for i in range(1, rows):
            for j in range(1, cols):
                cost[i][j] = min(cost[i - 1][j], cost[i][j - 1]) + grid[i][j]
        
        return cost[-1][-1]
    

cst = Solution()
print(cst.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))