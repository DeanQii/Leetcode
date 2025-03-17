
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # find the length of linkedlist
        n = 0
        cur = head
        while cur:
            n+=1
            cur = cur.next
        
        # dummy points to head
        dummy = ListNode(next = head)
        # get a p0 as fault pre to reverse linkedlist
        p0 = dummy

        #init pre and cur for reversing(first time)
        pre = None
        cur = p0.next
        while n>=k:
            n-=k
            # reverse link within the sublist
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
        
            nxt = p0.next
            # head of sublist -> tail
            p0.next.next = cur
            # tail of sublist -> head
            p0.next = pre\
            # get a new p0 for next reverse
            # notice the new p0 is the tail of reversed sublist, head of sublist(p0.next before head tail switch)
            # nxt = p0.next should be recorded the head tail switch
            p0 = nxt
        return dummy.next
            
        
        
