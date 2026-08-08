class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        last = [-1] * m
        p1 = n - 1

        for p2 in range(m-1, -1, -1):
            while p1 >= 0 and word1[p1] != word2[p2]:
                p1 -= 1
            if p1 >= 0:
                last[p2] = p1
                p1 -= 1
        
        ans = []
        changed = False
        p1 = 0

        for p2 in range(m):
            while p1 < n:
                is_match = word1[p1] == word2[p2]
                suffix = (p2 == m-1) or (last[p2+1] > p1)

                if is_match:
                    if not changed or suffix:
                        ans.append(p1)
                        p1 += 1
                        break
                elif not changed and suffix:
                    ans.append(p1)
                    changed = True
                    p1 += 1
                    break
                
                p1 += 1
        
        return ans if len(ans) == m else []
