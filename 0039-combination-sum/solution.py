class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, cur_sum, path):
            if cur_sum == target:
                res.append(path.copy())
                return
            if cur_sum > target or i >= len(candidates):
                return

            path.append(candidates[i])
            backtrack(i, cur_sum + candidates[i], path)

            path.pop()
            backtrack(i+1, cur_sum, path)

        backtrack(0, 0, [])

        return res
