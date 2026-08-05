class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)
        
        sups = set()
        queue = deque([k])
        sups.add(k)

        while queue:
            curr = queue.pop()
            for neighbour in graph[curr]:
                if neighbour not in sups:
                    sups.add(neighbour)
                    queue.append(neighbour)
        
        for u in range(n):
            if u not in sups:
                for v in graph[u]:
                    if v in sups:
                        return list(range(n))
        
        return [i for i in range(n) if i not in sups]
