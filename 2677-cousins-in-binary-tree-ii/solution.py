# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque([root])
        root.val = 0

        while queue:
            level = len(queue)
            total = 0
            curr_lvl_node = []

            for _ in range(level):
                node = queue.popleft()
                curr_lvl_node.append(node)

                if node.left:
                    total += node.left.val
                    queue.append(node.left)
                if node.right:
                    total += node.right.val
                    queue.append(node.right)

            for node in curr_lvl_node:
                sb_sum = 0
                if node.left: sb_sum += node.left.val
                if node.right: sb_sum += node.right.val

                if node.left:
                    node.left.val = total - sb_sum
                if node.right:
                    node.right.val = total - sb_sum
        
        return root
