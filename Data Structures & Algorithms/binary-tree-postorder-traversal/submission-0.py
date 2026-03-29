# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return []
        def inorder(node: Optional[TreeNode]):
            order = []
            if node != None: 

                order.extend(inorder(node.left))
                order.extend(inorder(node.right))
                order.append(node.val)

            return order
        return inorder(root)
            