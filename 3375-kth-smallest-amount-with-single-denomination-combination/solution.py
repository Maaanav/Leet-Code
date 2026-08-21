class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        subsets = []
        for r in range(1, n+1):
            sign = 1 if r%2 == 1 else -1
            for combo in combinations(coins, r):
                lcm_val = combo[0]
                for coin in combo[1:]:
                    lcm_val = math.lcm(lcm_val, coin)
                subsets.append((lcm_val, sign))
        

        def count_mult(x: int) -> int:
            total = 0
            for lcm_val, sign in subsets:
                total += sign * (x // lcm_val)
            return total

        left = 1
        right = min(coins) * k
        res = right

        while left <= right:
            mid = (left + right) // 2
            if count_mult(mid) >= k:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res 
