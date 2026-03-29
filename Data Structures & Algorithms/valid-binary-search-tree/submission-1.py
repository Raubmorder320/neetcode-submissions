# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
            if root == None: return []
            def inorder(node: Optional[TreeNode]):
                order = []
                if node != None: 

                    order.extend(inorder(node.left))
                    order.append(node.val)
                    order.extend(inorder(node.right))
                return order
            return inorder(root)
        order = inorderTraversal(root)
        return order == sorted(list(set(order)))