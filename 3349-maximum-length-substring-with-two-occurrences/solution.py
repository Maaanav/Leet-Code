class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        freq = defaultdict(int)
        max_len = 0
        i = 0
        for j in range(len(s)):
            freq[s[j]] += 1
            while freq[s[j]] > 2:
                freq[s[i]] -= 1
                i += 1

            max_len = max(max_len, j - i + 1)
        return max_len            
