class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        res = []

        for i in range(len(nums)-1):
            curr = nums[i]
            next_num = nums[i+1]

            if next_num - curr > 1:
                for missing in range(curr+1, next_num):
                    res.append(missing)
        
        return res
