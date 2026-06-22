class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        for count, char in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if count > 0:
                heapq.heappush(max_heap, (-count, char))
        res = []

        while max_heap:
            count1, char1 = heapq.heappop(max_heap)
            count1 = -count1

            if len(res) >= 2 and res[-1] == char1 and res[-2] == char1:
                if not max_heap:
                    break
                count2, char2 = heapq.heappop(max_heap)
                count2 = -count2

                res.append(char2)
                count2 -= 1

                if count2 > 0:
                    heapq.heappush(max_heap, (-count2, char2))
            
                heapq.heappush(max_heap, (-count1, char1))
            else:
                res.append(char1)
                count1 -= 1

                if count1 > 0:
                    heapq.heappush(max_heap, (-count1, char1))
            
        return "".join(res)
            



