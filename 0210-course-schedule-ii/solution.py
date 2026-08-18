class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[v].append(u)
        
        state = [0] * numCourses
        stack = []

        def dfs(curr: int) -> bool:
            if state[curr] == 1:
                return False
            if state[curr] == 2:
                return True
            state[curr] = 1

            for neighbor in adj[curr]:
                if not dfs(neighbor):
                    return False
            
            state[curr] = 2
            stack.append(curr)
            return True

        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return []

        return stack[::-1]
