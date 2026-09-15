class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        last_end = -1  

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for i in range(k - 1, n):
            if i - k + 1 > last_end and is_palindrome(i - k + 1, i):
                ans += 1
                last_end = i
            elif i - k >= 0 and i - k > last_end and is_palindrome(i - k, i):
                ans += 1
                last_end = i

        return ans
    
