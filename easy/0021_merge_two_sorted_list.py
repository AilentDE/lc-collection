from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


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

    list1 = list_to_linkedlist([1, 2, 4])
    list2 = list_to_linkedlist([1, 3, 4])
    sol1 = s.mergeTwoLists(list1, list2)
    assert linkedlist_to_list(sol1) == [1, 1, 2, 3, 4, 4]

    list3 = list_to_linkedlist([])
    list4 = list_to_linkedlist([])
    sol2 = s.mergeTwoLists(list3, list4)
    assert linkedlist_to_list(sol2) == []

    list5 = list_to_linkedlist([])
    list6 = list_to_linkedlist([0])
    sol3 = s.mergeTwoLists(list5, list6)
    assert linkedlist_to_list(sol3) == [0]
