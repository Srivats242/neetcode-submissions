# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.next = next

        palindrome_set = set()

        if not head:
            return False

        while (head != 0 and head == head + 1):
            head.next = next
            return True
        
        return self.isPalindrome(head.val)