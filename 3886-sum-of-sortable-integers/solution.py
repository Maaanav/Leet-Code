class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        
        def can_sort_block(block):
            m = len(block)
            drops = 0
            for i in range(m):
                if block[i] > block[(i + 1) % m]:
                    drops += 1
            return drops <= 1

        divisors = [k for k in range(1, n + 1) if n % k == 0]
        total_sum = 0

        for k in divisors:
            blocks = [nums[i:i + k] for i in range(0, n, k)]
            
            possible = True
            for block in blocks:
                if not can_sort_block(block):
                    possible = False
                    break
            
            if not possible:
                continue
                
            for i in range(len(blocks) - 1):
                if max(blocks[i]) > min(blocks[i + 1]):
                    possible = False
                    break
                    
            if possible:
                total_sum += k

        return total_sum
