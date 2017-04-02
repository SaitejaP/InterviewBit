# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.


class Solution:
    # @param A : string
    # @return an integer

    def isPalindrome(self, A):
        start = 0
        end = len(A) - 1

        if end == 0:
            return 1

        while start < end:
            while (start < end) and (not A[start].isalnum()):
                start += 1

            while (start < end) and (not A[end].isalnum()):
                end -= 1

            if A[start].lower() != A[end].lower():
                return 0

            start += 1
            end -= 1

        return 1

print Solution().isPalindrome("A man, a plan, a canal: Panama")
