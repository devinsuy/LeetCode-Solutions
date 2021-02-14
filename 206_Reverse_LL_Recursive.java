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
    public ListNode reverseUtil(ListNode curr, ListNode prev){
        // Base case, list full reversed
        if(curr == null)
            return prev;
        
        ListNode next = curr.next;
        curr.next = prev;
        return reverseUtil(next, curr);
    }
    
    public ListNode reverseList(ListNode head) {
        return this.reverseUtil(head, null);
    }
}