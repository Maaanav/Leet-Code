class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        def back_track(start: int, path: list[str]):
            if start == len(s):
                res.append(path.copy())
                return
            
            for end in range(start, len(s)):
                substring = s[start: end + 1]
                if is_palindrome(substring):
                    path.append(substring)
                    back_track(end + 1, path)
                    path.pop()
            
        back_track(0,[])
        return res

