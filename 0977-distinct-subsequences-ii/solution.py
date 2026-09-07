class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        last_added = [0] * 26
        total = 0

        for char in s:
            idx = ord(char) - ord('a')
            new_added = (total + 1 - last_added[idx]) % MOD
            total = (total + new_added) % MOD
            last_added[idx] = (last_added[idx] + new_added) % MOD
        
        return total
