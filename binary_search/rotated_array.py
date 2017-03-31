# Suppose a sorted array A is rotated at some pivot unknown to you beforehand.
# 
# Find the minimum element.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        if A[len(A)-1] > A[0]:
            return A[0]
            
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = int((start + end)/2)
            _next = (mid + 1) % len(A)
            _prev = (mid - 1) % len(A)
            if A[mid] <= A[_next] and A[mid] <= A[_prev]:
                return A[mid]
            elif A[mid] >= A[end]:
                start = mid + 1
            elif A[mid] < A[end]:
                end = mid - 1

print Solution().findMin([4, 5, 6, 7, 0, 1, 2])