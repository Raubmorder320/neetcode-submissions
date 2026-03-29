# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = []
        queue = deque()
        queue.append(root)
        node = root
        i = 0
        if not node: return []
        while queue:
            level = len(queue)
            lev = []

            for _ in range(level):
                node = queue.popleft()
                lev.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            order.append(lev)
            
        return order