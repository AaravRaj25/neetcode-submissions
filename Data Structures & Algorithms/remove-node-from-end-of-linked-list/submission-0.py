# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev1=dummy
        prev2=head

        for i in range(n):
            prev2=prev2.next
        while prev2:
            prev1=prev1.next
            prev2=prev2.next
        prev1.next=prev1.next.next
        return dummy.next

