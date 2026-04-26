class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for n in nums:
                if n not in visited:
                    visited.add(n)
                    path.append(n)

                    backtrack(path)

                    visited.remove(n)
                    path.pop()

        backtrack([])
        return res        
