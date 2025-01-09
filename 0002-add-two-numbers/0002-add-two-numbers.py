# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer_first = ListNode()
        answer = answer_first
        up = 0
        
        print(l1.val)
        while (l1 is not None) or (l2 is not None) or (up != 0):
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            s = l1_val + l2_val + up
            up = s // 10
            v = s % 10
            answer.val = v
            
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            if l1 is None and l2 is None and up == 0:
                break
            answer.next = ListNode()
            answer = answer.next
        return answer_first