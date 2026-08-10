class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        prev1, prev2 = 0, 0

        for i in range(len(nums)):
            curr = nums[i] * count[nums[i]]

            if i > 0 and nums[i] == nums[i-1] + 1:
                temp = prev1
                prev1 = max(curr + prev2, prev1)
                prev2 = temp
            else:
                prev2 = prev1
                prev1 += curr
        
        return prev1
