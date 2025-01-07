from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = head
        while result and result.next:
            if result.val == result.next.val:
                result.next = result.next.next
            else:
                result = result.next
        return head


if __name__ == "__main__":

    def list_to_linkedlist(lst):
        dummy = ListNode()
        current = dummy
        for value in lst:
            current.next = ListNode(value)
            current = current.next
        return dummy.next

    def linkedlist_to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    s = Solution()

    sol1 = s.deleteDuplicates(list_to_linkedlist([1, 1, 2]))
    assert linkedlist_to_list(sol1) == [1, 2]

    sol2 = s.deleteDuplicates(list_to_linkedlist([1, 1, 2, 3, 3]))
    assert linkedlist_to_list(sol2) == [1, 2, 3]
