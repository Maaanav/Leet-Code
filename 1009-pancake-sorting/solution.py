class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []

        for target in range(len(arr), 1, -1):
            indx = arr.index(target)

            if indx == target - 1:
                continue

            if indx != 0:
                res.append(indx+1)
                arr[:indx + 1] = reversed(arr[:indx + 1])

            res.append(target) 
            arr[:target] = reversed(arr[:target])
        
        return res

