class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for i in range(32):
            b_sum = 0

            for num in nums:
                b_sum += (num >> i) & 1

            if b_sum % 3 != 0:
                res |= (1 << i)

        if (res & (1 << 31)) != 0:
            res = res - (1 << 32)
        return res 
