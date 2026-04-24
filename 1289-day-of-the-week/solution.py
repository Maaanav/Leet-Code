class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weeks = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        months = [31,28,31,30,31,30,31,31,30,31,30,31]

        total = 0

        for y in range(1971, year):
            if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
                total += 366
            else:
                total += 365

        for m in range(1, month):
            total += months[m-1]  
            if m == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
                total += 1
        
        total += day

        return weeks[(total + 4) % 7]


