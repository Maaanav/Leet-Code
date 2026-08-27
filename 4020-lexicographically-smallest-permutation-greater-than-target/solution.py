class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        s_counts = Counter(s)

        def try_prefix(p: int) -> str:
            counts = s_counts.copy()

            for i in range(p):
                char = target[i]
                if counts[char] > 0:
                    counts[char] -= 1
                else:
                    return ""
            pivot_char = None
            for ch_code in range(ord(target[p]) + 1, ord('z') + 1):
                ch = chr(ch_code)
                if counts[ch] > 0:
                    pivot_char = ch
                    counts[ch] -=1
                    break
            if not pivot_char:
                return ""
            
            suffix = []
            for ch_code in range(ord('a'), ord('z') + 1):
                ch = chr(ch_code)
                if counts[ch] > 0:
                    suffix.append(ch * counts[ch])
            
            return target[:p] + pivot_char + "".join(suffix)

        for p in range(n-1, -1, -1):
            result = try_prefix(p)
            if result:
                return result
        
        return ""
