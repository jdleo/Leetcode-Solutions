# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # pointer for previous node
        prev = None

        # while there are nodes to reverse
        while head:
            # get cur
            cur = head
            # move head forward
            head = head.next
            # set curs next to prev
            cur.next = prev
            # set prev
            prev = cur

        return prev