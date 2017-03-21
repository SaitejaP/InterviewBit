# Given an unsorted array, find the maximum difference between the successive 
# elements in its sorted form.
# 
# Try to solve it in linear time/space.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if len(A) < 2: return 0
        
        A = sorted(A)
        max_diff = float('-inf')
        for i in range(len(A)-1):
            diff = A[i+1] - A[i]
            if diff > max_diff:
                max_diff = diff
        return max_diff

print(Solution().maximumGap([2,3,43,22,1]))