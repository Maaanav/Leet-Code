class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_counts = Counter()
        res = 0

        for u in nums1:
            for v in nums2:
                sum_counts[u + v] += 1
        
        for x in nums3:
            for y in nums4:
                target = -(x + y)
                if target in sum_counts:
                    res += sum_counts[target]
        return res
