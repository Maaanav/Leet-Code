class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split("-"))

        months = [31,28,31,30,31,30,31,31,30,31,30,31]

        res = sum(months[:month-1]) + day

        if month > 2:
            if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                res += 1
        
        return res
        
