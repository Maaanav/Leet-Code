class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        name_len, typed_len = len(name), len(typed)

        while j < typed_len:
            if i < name_len and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and name[i-1] == typed[j]:
                j += 1
            else:
                return False

        return i == name_len 
        
