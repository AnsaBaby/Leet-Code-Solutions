from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        currentNode = dummyHead
        carryOver = 0
        while list1 is not None or list2 is not None or carryOver != 0:
            list1Value = list1.val if list1 else 0
            list2Value = list2.val if list2 else 0
            columnSum = list1Value + list2Value + carryOver
            carryOver = columnSum // 10
            newNode = ListNode(columnSum % 10)
            currentNode.next = newNode
            currentNode = newNode
            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None
        return dummyHead.next
    
# Time Complexity: O(n)
# Space Complexity: O(n)