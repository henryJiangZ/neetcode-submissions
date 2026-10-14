# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def search(root: Optional[TreeNode]):
            if not root:
                return
            search(root.left)
            if root.left is not None:
                result.append(root.left.val)
            search(root.right)
            if root.right is not None:
                result.append(root.right.val)
        
        search(root)
        if root is not None:
            result.append(root.val)
        return result