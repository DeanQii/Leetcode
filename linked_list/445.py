
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    reverse list
    while one of node is not None:
        add val
        pass 10
    key: which is long/create a long
    '''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = l1
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        #current node of l1
        cur1 = pre

        pre = None
        cur = l2
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        cur2 = pre
        head = ListNode()
        cur = head
        while cur1 and cur2:
            sum2 = cur1.val + cur2.val
            cur.val += sum2
            if cur.val//10:
                cur.val %= 10
                temp = ListNode(val = 1)
                cur.next = temp
                cur = temp
            elif cur1.next or cur2.next:
                temp = ListNode()
                cur.next = temp
                cur = temp
            cur1 = cur1.next
            cur2 = cur2.next
        
        while cur1:
            cur.val += cur1.val
            if cur.val >= 10:
                cur.val = cur.val%10
                temp = ListNode(val = 1)
                cur.next = temp
                cur = temp
            elif cur1.next:
                temp =  ListNode()
                cur.next = temp
                cur = temp
            
            cur1 = cur1.next

        while cur2:
            cur.val += cur2.val
            if cur.val >= 10:
                cur.val = cur.val%10
                temp = ListNode(val = 1)
                cur.next = temp
                cur = temp
            elif cur2.next:
                temp =  ListNode()
                cur.next = temp
                cur = temp
            
            cur2 = cur2.next
        
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
            
