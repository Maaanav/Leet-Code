# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        
        queue = deque([root])

        while queue:
            level = len(queue)
            x_found = False
            y_found = False

            for _ in range(level):
                node = queue.popleft()

                if node.left and node.right:
                    left_val = node.left.val
                    right_val = node.right.val
                    if (left_val == x and right_val == y) or (left_val == y and right_val == x):
                        return False
                
                if node.left:
                    if node.left.val == x: x_found = True
                    if node.left.val == y: y_found = True
                    queue.append(node.left)
                
                if node.right:
                    if node.right.val == x: x_found = True
                    if node.right.val == y: y_found = True
                    queue.append(node.right)
                
            if x_found and y_found:
                return True
            
            if x_found or y_found:
                return False
        
        return False
