# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        def bfs(node):
            if not node:
                return 

            bfs(node.left)
            bfs(node.right)
            res.append(node.val)
        
        bfs(root)
        return res
        
