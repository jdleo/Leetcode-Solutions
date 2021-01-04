# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # result
        res = 0

        # while there are still nodes to process
        while head:
            # left shift res
            res <<= 1
            # OR current bit with res
            res |= head.val
            # go to next node
            head = head.next

        return res