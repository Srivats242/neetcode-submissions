# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Correct Solution

        fast = head
        slow = head

        # Find middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse second half of the list
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        # Check if its a palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

        # My Solution
        #self.next = next

        #palindrome_set = set()

        #if not head:
           # return False

        #if (head.node != 0):
            #palindrome_set.append(head)
            #head.next = next
            #return True
        
        #return True