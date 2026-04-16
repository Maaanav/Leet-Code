class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        distance = 0

        for i in range(n-1, -1, -1):
            if colors[i] != colors[0]:
                distance = i
                break

        for i in range(n):
            if colors[i] != colors[-1]:
                distance = max(distance, n - 1 - i)
                break
        
        return distance
