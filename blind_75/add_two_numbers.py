#https://leetcode.com/problems/add-two-numbers/submissions/1534143587/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class SolutionOptimized:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        pointer = answer
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            total = l1_value + l2_value + carry
            carry = total // 10
            answer.next = ListNode(total % 10)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            answer = answer.next
        return pointer.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        pointer = answer
        while l1 is not None and l2 is not None:
            total = l1.val + l2.val
            tens = int(total / 10)
            ones = total % 10
            tmp_answer = answer.val + ones
            answer.val = tmp_answer % 10
            carry = tens + int(tmp_answer / 10)
            if l1.next is None and l2.next is not None:
                l1.next = ListNode()
            if l2.next is None and l1.next is not None:
                l2.next = ListNode()
            if (l1.next is not None and l2.next is not None) or (l1.next is None and l2.next is None and carry != 0):
                answer.next = ListNode(val=carry) 
            l1 = l1.next
            l2 = l2.next
            answer = answer.next
        return pointer

class Solution_two:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_val = ""
        l2_val = ""
        ptr = None
        while l1 is not None:
            l1_val += str(l1.val)
            l1 = l1.next
        while l2 is not None:
            l2_val += str(l2.val)
            l2 = l2.next
        if len(l1_val) < len(l2_val):
            l1_val = l1_val + "".join(["0" for i in range(len(l2_val) - len(l1_val))])
        if len(l2_val) < len(l1_val):
            l1_val = l1_val + "".join(["0" for i in range(len(l1_val) - len(l2_val))])
        total = int(l1_val[::-1]) + int(l2_val[::-1])
        reversed_total = str(total)[::-1]
        for i in range(len(reversed_total)):
            if i == 0:
                answer = ListNode(val = int(reversed_total[i]))
                ptr = answer
            else:
                answer.val = int(reversed_total[i])
            if i != len(reversed_total) - 1:
                answer.next = ListNode()
            answer = answer.next
        return ptr

