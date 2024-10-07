

# Definition for a Node.
class Node:
    def __init__(self, val: [int] = None, children: [list['Node']] = None): # type: ignore
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        if not root:
            return
        stk = []
        stk.append(root)
        res = []

        while stk:
            node = stk.pop()
            res.append(node.val)

            stk.extend(node.children)
        return reversed(res)