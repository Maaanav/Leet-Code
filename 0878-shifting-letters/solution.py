class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = list(s)
        run_shift = 0

        for i in range(len(s) -1, -1, -1):
            run_shift = (run_shift + shifts[i]) % 26
            curr_pos = ord(res[i]) - ord('a')
            new_pos = (curr_pos + run_shift) % 26
            res[i] = chr(new_pos + ord('a')) 
        
        return "".join(res)
        
