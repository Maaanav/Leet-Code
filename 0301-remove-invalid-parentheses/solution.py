class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        rem_open = 0
        rem_close = 0
        for char in s:
            if char == '(':
                rem_open += 1
            elif char == ')':
                if rem_open > 0:
                    rem_open -= 1
                else:
                    rem_close += 1

        res = set()

        def dfs(index: int, open_count: int, close_count: int, rem_o: int, rem_c: int, path: list):
            if index == len(s):
                if rem_o == 0 and rem_c == 0:
                    res.add("".join(path))
                return
            
            char = s[index]

            if char == '(' and rem_o > 0:
                dfs(index + 1, open_count, close_count, rem_o - 1, rem_c, path)
            elif char == ')' and rem_c > 0:
                dfs(index + 1, open_count, close_count, rem_o, rem_c - 1, path)
            
            path.append(char)
            if char not in '()':
                dfs(index + 1, open_count, close_count, rem_o, rem_c, path)
            elif char == '(':
                dfs(index + 1, open_count + 1, close_count, rem_o, rem_c, path)
            elif char == ')' and open_count > close_count:
                dfs(index + 1, open_count, close_count + 1, rem_o, rem_c, path)
            path.pop()
        
        dfs(0,0,0, rem_open, rem_close, [])
        return list(res)
