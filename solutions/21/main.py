# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # dummy head and head to return
        head = ListNode(-1)
        dummy = head

        # go while there are still nodes to take
        while l1 or l2:
            # get values of nodes, but max value if null (since comparing min)
            v1 = l1.val if l1 else float('inf')
            v2 = l2.val if l2 else float('inf')

            # compare values
            if v1 <= v2:
                # choose l1 as next node, move l1 forward
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next
            else:
                # choose l2 as next node, move l2 forward
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next

        # return next node since head is the -1 dummy node
        return head.next