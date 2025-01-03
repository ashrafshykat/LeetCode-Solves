class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False  # if x is negative, it cannot be a palindrome
        return str(x) == str(x)[::-1]

    # str(x)[::-1]: Reverses the string representation of x.
    # The slicing [::-1] starts at the end of the string and moves backward to reverse it.
