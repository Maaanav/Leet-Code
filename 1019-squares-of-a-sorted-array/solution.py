class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = collections.deque()
        l, r = 0 , len(nums) -1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                res.appendleft(left*left)
                l += 1
            else:
                res.appendleft(right*right)
                r -= 1
        
        return list(res)
