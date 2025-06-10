from itertools import pairwise
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[int[int]]:
        pascal = [[1]]

        for i in range(numRows - 1):
            x = [1] + [a+b for a, b in pairwise(pascal[-1])] + [1]
            pascal.append(x)
        return pascal