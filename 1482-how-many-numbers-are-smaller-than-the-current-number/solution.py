class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted((nums))

        d = {}

        for j, num in enumerate(temp):
            if num not in d:
                d[num] = j
        
        res = []

        for i in nums:
            res.append(d[i])

        return res


        
