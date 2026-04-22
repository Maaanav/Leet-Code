class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count_map = [0] * 101 
        for h in heights:
            count_map[h] += 1

        res = 0
        curr_height = 0

        for h in heights:
            while count_map[curr_height] == 0:
                curr_height += 1

            if h != curr_height:
                res += 1
            
            count_map[curr_height] -= 1
        
        return res


