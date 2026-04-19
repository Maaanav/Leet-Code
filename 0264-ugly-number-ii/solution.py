class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2, i3, i5 = 0, 0, 0

        for i in range(1, n):
            next_n = min(
                nums[i2] * 2, nums[i3] * 3, nums[i5] * 5
            )

            nums.append(next_n)
            if next_n == nums[i2] * 2:
                i2 += 1
            if next_n == nums[i3] * 3:
                i3 += 1
            if next_n == nums[i5] * 5:
                i5 += 1
            
        return nums[n-1]
