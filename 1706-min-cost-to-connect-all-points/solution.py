class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        visited = [False] * n
        mst = 0

        for _ in range(n):
            curr = -1
            for i in range(n):
                if not visited[i] and (curr == -1 or min_dist[i] < min_dist[curr]):
                    curr = i
            visited[curr] = True
            mst += min_dist[curr]

            x1, y1 = points[curr]
            for v in range(n):
                if not visited[v]:
                    x2, y2 = points[v]
                    dist = abs(x2 - x1) + abs(y2 - y1)
                    min_dist[v] = min(min_dist[v], dist)
            
        return mst
