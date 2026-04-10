class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:

        if indexDiff < 0:
            return False
        
        buckets = {}
        width = valueDiff+1

        for i,n in enumerate(nums):
            bucket_id = n // width

            if bucket_id in buckets:
                return True
            
            if (bucket_id - 1) in buckets and abs(n - buckets[bucket_id - 1]) <= valueDiff:
                return True
            
            if (bucket_id + 1) in buckets and abs(n - buckets[bucket_id + 1]) <= valueDiff:
                return True

            buckets[bucket_id] = n

            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // width]
        
        return False

        
