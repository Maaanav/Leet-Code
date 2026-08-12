class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        max_freq = 0
        i = 0
        freqCount = defaultdict(int)

        for j in range(len(nums)):
            freqCount[nums[j]] += 1 
            
            while freqCount[nums[j]] > k:
                freqCount[nums[i]] -= 1
                i += 1
            
            max_freq = max(max_freq, j - i + 1)
        
        return max_freq
        
                
