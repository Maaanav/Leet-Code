class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        num_str = [str(num) for num in nums]

        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        num_str.sort(key=cmp_to_key(compare))

        res = "".join(num_str)

        return "0" if res[0] == "0" else res
