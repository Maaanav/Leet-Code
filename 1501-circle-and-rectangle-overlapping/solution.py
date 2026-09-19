class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x = max(x1, min(x2, xCenter))
        y = max(y1, min(y2, yCenter))

        dx = x - xCenter
        dy = y - yCenter

        return (dx * dx + dy * dy) <= (radius * radius)
