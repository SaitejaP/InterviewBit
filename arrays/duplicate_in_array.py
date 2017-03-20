# Given a read only array of n + 1 integers between 1 and n, find one number that 
# repeats in linear time using less than O(n) space and traversing the stream 
# sequentially O(1) times.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        if len(A) <= 1: return -1

        obj = {}
        for i in range(len(A)):
            try:
                obj[A[i]]
                return A[i]
            except KeyError:
                obj[A[i]] = 1
        return -1

print(Solution().repeatedNumber([2, 3, 4, 2, 5]))