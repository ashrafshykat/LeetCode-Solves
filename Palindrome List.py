# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: int[ListNode]) -> bool:
        vals = []  # store the values of the nodes in a list
        current_node = head  # start from the head of the linked list
        while current_node is not None:  # iterate through the linked list
            vals.append(
                current_node.val
            )  # add the value of the current node to the list
            current_node = current_node.next  # move to the next node
        return vals == vals[::-1]  # check if the list of values is a palindrome
