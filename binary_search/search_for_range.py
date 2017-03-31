# Given a sorted array of integers, find the starting and ending position of a given target value.
# 
# Your algorithm’s runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        lenA = len(A)
        start = 0
        end = lenA - 1
        lower_index = -1
        higher_index = -1
        
        while start <= end:
            mid = (start + end) / 2
            if A[mid] == B:
                lower_index = mid
                end = mid - 1
            elif A[mid] > B:
                end = mid - 1
            else:
                start = mid + 1
        
        if lower_index == -1:
            return [lower_index, higher_index]
        
        start = lower_index
        end = lenA - 1
        while start <= end:
            mid = (start + end) / 2
            if A[mid] == B:
                higher_index = mid
                start = mid + 1
            elif A[mid] > B:
                end = mid - 1
            else:
                start = mid + 1
        
        return [lower_index, higher_index]

print Solution().searchRange([-23, 0, 2, 4, 4, 80, 99], 4)