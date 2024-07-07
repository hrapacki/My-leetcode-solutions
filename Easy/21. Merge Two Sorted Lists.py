# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        ptr = list3 # both used to point to the same node
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next
        if list1 is not None:
            ptr.next = list1
        elif list2 is not None:
            ptr.next = list2
        return list3.next