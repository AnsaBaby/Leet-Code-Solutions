/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head= new ListNode();
        var currentNode = head;
        int sum=0; int carryOver=0; 

        while(l1!=null || l2!=null)
        {
           sum = (l1==null? 0: l1.val )+ (l2 == null? 0: l2.val) + carryOver;
           currentNode.next = new ListNode(sum % 10);
           currentNode = currentNode.next;

           carryOver = sum/10;
           l1= l1?.next;
           l2= l2?.next;
        }

        if(carryOver!= 0)
        {
            currentNode.next = new ListNode(carryOver);
        }

        return head.next;
    }
}
