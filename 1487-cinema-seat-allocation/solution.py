class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_rows = defaultdict(int)

        for row, col in reservedSeats:
            if 2 <= col <= 9:
                reserved_rows[row] |= (1 << (col-2))
        
        groupA = (1 << 0) | (1 << 1) | (1 << 2) | (1 << 3)
        groupB = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        groupC = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)

        res = (n - len(reserved_rows)) * 2
        
        for mask in reserved_rows.values():

            if ((mask & groupA) == 0) and ((mask & groupC) == 0):
                res += 2
            elif ((mask & groupA) == 0) or ((mask & groupB) == 0) or ((mask & groupC) == 0):
                res += 1
        
        return res



