class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[v].append(u)
        
        state = [0] * numCourses

        def is_cycle(curr: int) -> bool:
            if state[curr] == 1:
                return True
            if state[curr] == 2:
                return False
            
            state[curr] = 1

            for neighbor in adj[curr]:
                if is_cycle(neighbor):
                    return True
            
            state[curr] = 2
            return False
        
        for i in range(numCourses):
            if state[i] == 0:
                if is_cycle(i):
                    return False
        
        return True


