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
    public int getDecimalValue(ListNode head) {

        int dv = 0;
        ListNode curr = head;
        int length = 0;

        while(curr != null){
            length++;
            curr = curr.next;
        }

        curr = head;
        int power = length-1;

        while(curr != null){
            dv += curr.val * Math.pow(2,power);
            power--;
            curr = curr.next; 
        }

        return dv;
    }
}
