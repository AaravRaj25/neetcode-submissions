# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def length(head):
            count = 0
            curr = head

            while curr:
                count += 1
                curr = curr.next

            return count

        def extractNumber(head):
            number = 0
            curr = head

            for i in range(length(head)):
                number += curr.val * (10 ** i)
                curr = curr.next

            return number

        def createList(num):
            dummy = ListNode(0)
            curr = dummy

            if num == 0:
                return ListNode(0)

            while num > 0:
                digit = num % 10
                curr.next = ListNode(digit)
                curr = curr.next
                num = num // 10

            return dummy.next

        total = extractNumber(l1) + extractNumber(l2)

        return createList(total)
                
        
            


        