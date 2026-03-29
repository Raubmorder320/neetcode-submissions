# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return []
        def inorder(node: Optional[TreeNode]):
            order = []
            if node != None: 
                order.append(node.val)

                order.extend(inorder(node.left))
                order.extend(inorder(node.right))
            return order
        return inorder(root)
            