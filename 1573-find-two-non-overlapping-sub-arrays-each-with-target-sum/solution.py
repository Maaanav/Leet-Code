class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        min_len = [float('inf')] * n
        prefix_map = {0: -1}

        curr_sum = 0
        min_so_far = float('inf')
        res = float('inf')

        for i, val in enumerate(arr):
            curr_sum += val
            if curr_sum - target in prefix_map:
                prev_idx = prefix_map[curr_sum - target]
                curr_len = i - prev_idx

                if prev_idx >= 0 and min_len[prev_idx] != float('inf'):
                    res = min(res, curr_len + min_len[prev_idx])

                min_so_far = min(min_so_far, curr_len)

            min_len[i] = min_so_far
            prefix_map[curr_sum] = i

        return -1 if res == float('inf') else res 
