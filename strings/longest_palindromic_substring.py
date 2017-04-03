# Given a string S, find the longest palindromic substring in S.


class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        lenA = len(A)
        max_start = 0
        max_end = 0
        for i in range(lenA - 1):
            # check for immediate next
            start = -1
            end = -1

            if A[i] == A[i+1]:
                start = i
                end = i+1
            if start >= 0 and end >= 0: # if palindrome starts
                while (start >= 0) and (end < lenA) and (A[start] == A[end]):
                    start-=1
                    end+=1
                start+=1
                end-=1
                diff = end - start
                max_diff = max_end - max_start
                if (diff > max_diff) or (diff == max_diff and start < max_start):
                    max_start = start
                    max_end = end

            # check for alternate                       
            if i+2 < lenA:
                start = -1
                end = -1
                if A[i] == A[i+2]:
                    start = i
                    end = i+2
                if start >= 0 and end >= 0: # if palindrome starts
                    while (start >= 0) and (end < lenA) and (A[start] == A[end]):
                        start-=1
                        end+=1
                    start+=1
                    end-=1
                    diff = end - start
                    max_diff = max_end - max_start
                    if (diff > max_diff) or (diff == max_diff and start < max_start):
                        max_start = start
                        max_end = end
        
        res = ''                    
        for i in range(max_start, max_end+1):
           res+=A[i]
        return res
        
print Solution().longestPalindrome('sdsjkdcnsdcdsncdksdshjh')
