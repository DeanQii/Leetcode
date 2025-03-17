
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        p0 = dummy

        pre = p0
        cur = p0.next
        while cur and cur.next!=None:
            # one pair reverse
            for _ in range(2):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            p0.next.next = cur
            p0.next = pre
            p0 = pre.next
        return dummy.next


        
