class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0

        res = 0
        i = 1

        while i < n-1:
            if arr[i-1] < arr[i] > arr[i+1]:
                l = i - 1

                while l > 0 and arr[l-1] < arr[l]:
                    l -= 1
                
                r = i+1
                while r < n-1 and arr[r] > arr[r+1]:
                    r += 1
                
                res = max(res, r-l+1)
                i = r
            else:
                i +=1
        
        return res
        
