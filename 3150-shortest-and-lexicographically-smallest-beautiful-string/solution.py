class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res = ""
        count = 0
        i = 0

        for j in range(len(s)):
            if s[j] == '1':
                count += 1
            
            while count == k:
                temp = s[i: j+1]
                if not res or len(temp) < len(res) or (len(temp) == len(res) and temp < res):
                    res = temp
                
                if s[i] == '1':
                    count -= 1
                i += 1
        return res
