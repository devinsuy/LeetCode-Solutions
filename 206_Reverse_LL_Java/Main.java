package com.company;

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        ListNode tail = new ListNode(5, null);
        ListNode t2 = new ListNode(4, tail);
        ListNode t3 = new ListNode(3, t2);
        ListNode t4 = new ListNode(2, t3);
        ListNode head = new ListNode(1, t4);

        ListNode new_head = s.reverseList(head);
        ListNode curr = new_head;

        while(curr != null){
            System.out.println(curr.val);
            curr = curr.next;
        }
    }
}
