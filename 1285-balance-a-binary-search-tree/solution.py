# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        nodes = []
        stack = []
        curr  = root

        while stack or curr:

            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            nodes.append(curr.val)
            curr = curr.right

        if not nodes :
            return None

        n = len(nodes)
        mid = n//2
        root = TreeNode(nodes[mid])

        q = deque()
        q.append((root,0,mid-1))
        q.append((root,mid+1,n-1))

        while q:
            parent, left, right = q.popleft()
            if left <= right:
                mid = (left+right) // 2
                child = TreeNode(nodes[mid])
                if nodes[mid] < parent.val:
                    parent.left = child
                else:
                    parent.right = child
                q.append((child,left, mid-1))
                q.append((child, mid+1, right)) 
        
        return root
        
