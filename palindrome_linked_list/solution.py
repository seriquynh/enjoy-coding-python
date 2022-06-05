class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head.next is None:
            return True

        values = []

        current = head

        while current is not None:
            values.append(current.val)

            current = current.next

        return self.list_is_palindrome(values)

    @staticmethod
    def list_is_palindrome(values: list) -> bool:
        left = 0
        size = len(values)
        right = size - 1

        while left < right:
            if values[left] != values[right]:
                return False
            left = left + 1
            right = right - 1

        return True
