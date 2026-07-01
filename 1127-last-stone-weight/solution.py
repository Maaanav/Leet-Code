class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            st1 = -heapq.heappop(max_heap)
            st2 = -heapq.heappop(max_heap)

            if st1 != st2:
                new_st = st1 - st2
                heapq.heappush(max_heap, -new_st)
        
        return -max_heap[0] if max_heap else 0
