class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        d_counts = Counter(digits)
        res = 0

        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num//10) % 10
            d3 = num % 10

            req = Counter([d1, d2, d3])

            if all(d_counts[d] >= count for d, count in req.items()):
                res += 1
        
        return res

