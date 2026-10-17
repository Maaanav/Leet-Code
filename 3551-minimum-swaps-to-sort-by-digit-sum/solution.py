class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(n: int) -> int:
            return sum(int(d) for d in str(n))
        
        n = len(nums)
        
        target = sorted((get_digit_sum(x), x) for x in nums)
        
        target_pos = {val: i for i, (_, val) in enumerate(target)}
        
        visited = [False] * n
        cycles = 0
        
        for i in range(n):
            if not visited[i]:
                cycles += 1
                curr = i
                while not visited[curr]:
                    visited[curr] = True
                    curr = target_pos[nums[curr]]
                    
        return n - cycles
