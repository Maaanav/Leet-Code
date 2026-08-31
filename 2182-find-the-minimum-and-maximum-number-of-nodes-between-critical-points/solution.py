# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1,-1]

        # def iscritical(curr, prev, nxt) -> bool:
        #     return (prev.val < curr.val > nxt.val or prev.val > curr.val < nxt.val)

        prev = head
        curr = head.next
        index = 1

        first_cp = -1
        prev_cp = -1
        min_dist = float('inf')

        while curr.next:
            nxt = curr.next
            # if iscritical(curr, prev, nxt):
            if (prev.val < curr.val > nxt.val or prev.val > curr.val < nxt.val):
                if first_cp == -1:
                    first_cp = index
                else:
                    min_dist = min(min_dist, index - prev_cp)
                
                prev_cp = index
            
            prev = curr
            curr = nxt
            index += 1
        
        if first_cp == -1 or prev_cp == first_cp:
            return [-1, -1] 
        
        max_dist = prev_cp - first_cp
        return [min_dist, max_dist]

