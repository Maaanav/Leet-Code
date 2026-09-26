class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        kn_map = {k: v for k,v in knowledge}

        res = []
        temp = []
        in_key = False

        for char in s:
            if char == '(':
                in_key = True
                temp.clear()
            elif char == ')':
                in_key = False
                key_str = "".join(temp)
                res.append(kn_map.get(key_str, "?"))
            elif in_key:
                temp.append(char)
            else:
                res.append(char)
        
        return "".join(res)
