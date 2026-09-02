class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        discover_time = [-1] * n
        low = [-1] * n
        cc = []
        time = 0

        def dfs(curr: int, parent: int) -> None:
            nonlocal time
            discover_time[curr] = low[curr] = time
            time += 1

            for neighbor in adj[curr]:
                if neighbor == parent:
                    continue
                
                if discover_time[neighbor] == -1:
                    dfs(neighbor, curr)
                    low[curr] = min(low[curr], low[neighbor])

                    if low[neighbor] > discover_time[curr]:
                        cc.append([curr, neighbor])
                else:
                    low[curr] = min(low[curr], discover_time[neighbor])
                    
        dfs(0, -1)
        return cc
