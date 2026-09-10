# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0

        def countAverage(curr: TreeNode) -> tuple[int, int]:
            nonlocal res

            if not curr:
                return (0, 0)

            left_sum, left_count = countAverage(curr.left)
            right_sum, right_count = countAverage(curr.right)

            curr_sum = left_sum + right_sum + curr.val
            curr_count = left_count + right_count + 1

            if curr_sum // curr_count == curr.val:
                res += 1

            return (curr_sum, curr_count)

        countAverage(root)
        return res

