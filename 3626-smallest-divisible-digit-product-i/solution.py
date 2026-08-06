class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        def productfind(num: int) -> int:
            product = 1
            while num > 0: 
                d = num % 10 
                if d == 0:
                    return 0
                product *= d
                num //= 10 
            return product
        
        while True:
            if productfind(n) % t == 0:
                return n
            n += 1
