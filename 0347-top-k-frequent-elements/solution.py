class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] +=1
            else:
                count[num] = 1
        
        heap = []
        for num, freq in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq,num))
            elif freq > heap[0][0]:
                heapq.heapreplace(heap, (freq, num))
        
        top_k = [num for freq, num in heap]
        return top_k



        
