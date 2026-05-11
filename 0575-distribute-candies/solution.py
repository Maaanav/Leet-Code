class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        set_candy = set(candyType)
        
        return min(int(len(candyType) / 2), len(set_candy))

