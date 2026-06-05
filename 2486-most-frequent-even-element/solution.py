class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counts = Counter(num for num in nums if num % 2 == 0)
        if not counts:
            return -1
        
        ans = -1
        max_freq = 0

        for num, freq in counts.items():
            if freq > max_freq:
                max_freq = freq
                ans = num
            elif freq == max_freq:
                if num < ans:
                    ans = num
        
        return ans

