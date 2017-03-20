# -*- coding: utf-8 -*-
# You are given an array (zero indexed) of N non-negative integers, A0, A1, …, AN-1.
# Find the minimum sub array Al, Al+1, …, Ar so if we sort(in ascending order) 
# that sub array, then the whole array should get sorted.
# If A is already sorted, output -1.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        # check where the ascending order breaks
        i = 0
        while i < len(A)-1 and A[i] <= A[i+1]:
            i += 1
            
        # check where the descending order breaks
        j = len(A) - 1
        while j > 1 and A[j] >= A[j-1]:
            j -= 1
        
        # i loops till the end i.e., ascending 
        # order does not break, return [-1]
        if i == len(A)-1:
            return [-1]
        
        # find the min and max elements 
        # in the damaged area
        min_ele = A[i]
        max_ele = A[i]
        while i <= j:
            if A[i] < min_ele:
                min_ele = A[i]
            if A[i] > max_ele:
                max_ele = A[i]
            i += 1
        
        # find the position where min element can be inserted
        i = 0
        while i < len(A) and A[i] <= min_ele:
            i += 1
        
        # find the position where max element can be inserted
        j = len(A) - 1
        while j > 0 and A[j] >= max_ele:
            j -= 1
        
        return [i, j]
 
print Solution().subUnsort([16, 15, 16, 20])       
