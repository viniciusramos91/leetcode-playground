# 876. Middle of the Linked List
# ------------------------------
# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.
#
# Example:
#   Input: head = [1,2,3,4,5,6]
#   Output: [4,5,6]
#   Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head

        while tmp and tmp.next:
            head = head.next
            tmp = tmp.next.next

        return head



if __name__ == '__main__':
    s = Solution()
    l6 = ListNode(6)
    l5 = ListNode(5, l6)
    l4 = ListNode(4, l5)
    l3 = ListNode(3, l4)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)

    print(s.middleNode(l1).val)
