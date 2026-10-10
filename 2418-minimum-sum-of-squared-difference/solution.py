class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        d = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(d) <= k:
            return 0
        
        left, right = 0, max(d)

        while left < right:
            mid = (left + right) // 2
            if sum(max(0, v - mid) for v in d) <= k:
                right = mid
            else:
                left = mid + 1
                
        for i in range(len(d)):
            if d[i] > left:
                k -= (d[i] - left)
                d[i] = left
                
        for i in range(len(d)):
            if k > 0 and d[i] == left:
                d[i] -= 1
                k -= 1
                
        return sum(v * v for v in d)
