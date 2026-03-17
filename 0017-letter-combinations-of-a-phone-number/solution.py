class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        map = {
            "2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno",
            "7" : "pqrs", "8" : "tuv", "9": "wxyz"
        }

        res = []

        
        def backtrack(index, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            
            letters = map[digits[index]]

            for letter in letters:
                backtrack(index + 1, curr+letter)

        
        backtrack(0, "")
        return res
        
