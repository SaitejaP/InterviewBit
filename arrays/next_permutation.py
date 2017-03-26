# Implement the next permutation, which rearranges numbers into the numerically 
# next greater permutation of numbers.

class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        if len(A) <= 1: return A
        
        if A[-1] > A[-2]:
            A = self.swap(A, -1, -2)
            return A
        else:
            j = len(A)-1
            while(j>=0 and A[j] <= A[j-1]):
                j -= 1
            next_smallest_index = self.get_next_smallest_index(A, A[j-1], j, len(A)-1)
            A = self.swap(A, j-1, next_smallest_index)
            A = A[:j]+sorted(A[j:])
            return A
    
    def swap(self, arr, x, y):
        arr[x], arr[y] = arr[y], arr[x]
        return arr
    
    def get_next_smallest_index(self, arr, key, start, end):
        smallest_index = start
        for i in range(start+1, end+1):
            if arr[i] > key and arr[smallest_index] > arr[i]:
                smallest_index = i
        return smallest_index
        