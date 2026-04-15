class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob(houses):
            r1, r2 = 0, 0
            for n in houses:
                temp = max(n + r1, r2)
                r1 = r2
                r2 = temp
            return temp

        return max(rob(nums[:-1]), rob(nums[1:]))
