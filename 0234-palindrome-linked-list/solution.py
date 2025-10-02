# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while(fast) and (fast.next):
            slow = slow.next
            fast = fast.next.next

        prev = None

        while slow != None:
            n_pointer = slow.next
            slow.next = prev
            prev = slow
            slow = n_pointer
        
        left = head
        right = prev

        while right != None:
            if (right.val != left.val):
                return False
            left = left.next
            right = right.next
        
        return True




        
