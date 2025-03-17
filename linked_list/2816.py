
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverselist(head, mult = 1):
            pre = None
            cur = head
            while cur:
                cur.val = cur.val * mult
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre
        
        dummy = ListNode()
        p0 = dummy
        cur = reverselist(head,2)
        carry = 0
        while cur:
            p0.next = ListNode((cur.val+carry)%10)
            carry = (cur.val+carry)//10
            cur = cur.next
            p0 = p0.next
        if carry:
            p0.next = ListNode(carry)
        return reverselist(dummy.next)
