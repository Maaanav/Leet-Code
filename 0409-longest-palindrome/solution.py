class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        length = 0
        
        for char in s:
            if char in seen:
                seen.remove(char)
                length += 2
            else:
                seen.add(char)

        return length + 1 if seen else length
