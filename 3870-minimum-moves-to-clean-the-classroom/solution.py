class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start_pos = None
        litters = []

        for r in range(m):
            for c in range(n):
                cell = classroom[r][c]
                if cell == 'S':
                    start_pos = (r, c)
                elif cell == 'L':
                    litters.append((r, c))
                    
        num_litters = len(litters)
        target_mask = (1 << num_litters) - 1
        litter_map = {pos: i for i, pos in enumerate(litters)}

        init_mask = 0
        if start_pos in litter_map:
            init_mask |= (1 << litter_map[start_pos])
            
        if init_mask == target_mask:
            return 0

        queue = deque([(start_pos[0], start_pos[1], init_mask, energy, 0)])
        visited = {}
        visited[(start_pos[0], start_pos[1], init_mask)] = energy
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            r, c, mask, cur_energy, steps = queue.popleft()
            
            if cur_energy < 0:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_cell = classroom[nr][nc]
                    next_energy = cur_energy - 1
                    
                    if next_energy < 0:
                        continue
                        
                    next_mask = mask
                    
                    if next_cell == 'L':
                        litter_idx = litter_map[(nr, nc)]
                        next_mask |= (1 << litter_idx)
                        
                    if next_mask == target_mask:
                        return steps + 1

                    if next_cell == 'R':
                        next_energy = energy

                    state_key = (nr, nc, next_mask)
                    if state_key not in visited or visited[state_key] < next_energy:
                        visited[state_key] = next_energy
                        queue.append((nr, nc, next_mask, next_energy, steps + 1))
                        
        return -1
