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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head, curr, nxt, nxtnxt;
        int sum, currVal, carry, l1Val, l2Val;
        boolean hasCarry;
        carry = 0;
        
        // Initialize the first node as head
        sum = l1.val + l2.val;
        currVal = sum % 10;
        hasCarry = sum >= 10;
        if(hasCarry) carry = sum / 10;
        head = curr = new ListNode(currVal);
        
        l1 = l1.next;
        l2 = l2.next;
        
        // Iteratively sum the remaining nodes
        while(l1 != null || l2 != null){
            l1Val = (l1 != null) ? l1.val : 0;
            l2Val = (l2 != null) ? l2.val : 0;
            
            // Calculate the value for the new node
            sum = l1Val + l2Val;
            if(hasCarry) sum += carry;
            currVal = sum % 10;
            hasCarry = sum >= 10;
            if(hasCarry) carry = sum / 10;
            
            // Create and link the next node
            nxt = new ListNode(currVal);
            curr.next = nxt;
            curr = nxt;
            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;
        }
        // Link last node if there is a carry
        if(hasCarry) curr.next = new ListNode(carry);
        
        return head;
    }
}