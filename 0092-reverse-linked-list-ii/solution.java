/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if(head == null || head.next == null || left == right){
            return head;
        }

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode pre = dummy;

        for(int i=1; i<left; i++){
            pre = pre.next;
        }

        ListNode start = pre.next;
        ListNode curr = start.next;

        for(int i=left; i<right; i++){
            start.next = curr.next;
            curr.next = pre.next;
            pre.next = curr;
            curr = start.next;
        }
        return dummy.next;
    }
}
