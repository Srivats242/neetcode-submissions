
 //Definition for singly-linked list.
 /*public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}*/
 

class Solution {
    // My Solution
    /*public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
        ListNode current;
    }
    public boolean hasCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        int index = 0;
        while (head != null){
            //fast += 2;
            fast = fast.next;
            fast.next = fast.next.next;
            //slow += 1;
            slow = slow.next;

            if (fast.equals(slow)){
                return true;
            }
            if (index == -1){
                return false;
            }
        }
        if (head == null){
            return false;
        }
     //linkedList <Integer> = new linkedList<>();

        return true;
    }*/

    // Correct Solution
    public boolean hasCycle(ListNode head) {
        if (head == null){
            return false;
        }
        ListNode fast = head.next;
        ListNode slow = head;

        while (fast!= null && fast.next != null && slow != null){
            if (fast == slow){
                return true;
            }
            fast = fast.next.next;
            slow = slow.next;
        }
        return false;
    }
   
    
}
