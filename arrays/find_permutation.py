# Given a positive integer n and a string s consisting only of letters D
# or I, you have to find any permutation of first n positive integer that
# satisfy the given input string.

# D means the next number is smaller, while I means the next number is greater.


class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers

    def findPerm(self, A, B):
        count = 0
        for i in range(len(A)):
            if A[i] == 'I':
                count += 1
        start = B - count
        high = start + 1
        low = start - 1
        res = []
        res.append(start)
        for i in range(len(A)):
            if A[i] == 'I':
                res.append(high)
                high += 1
            elif A[i] == 'D':
                res.append(low)
                low -= 1
        return res

print Solution().findPerm('IDIIDIDIDI', 11)