class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        arr = sorted((l, r, w, i) for i, (l, r, w) in enumerate(intervals))
        n = len(arr)

        @functools.lru_cache(None)
        def dp(i: int, k: int):
            if i == n or k == 0:
                return (0, ())

            best_weight, best_indices = dp(i + 1, k)
            l, r, w, idx = arr[i]
            next_idx = bisect.bisect_right(arr, (r, math.inf))
            
            next_weight, next_indices = dp(next_idx, k - 1)
            pick_weight = w + next_weight
            pick_indices = tuple(sorted((idx,) + next_indices))

            if pick_weight > best_weight or (
                pick_weight == best_weight and pick_indices < best_indices
            ):
                return (pick_weight, pick_indices)

            return (best_weight, best_indices)

        return list(dp(0, 4)[1])
