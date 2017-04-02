# Find the longest common prefix string amongst an array of strings.

class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        if len(A) == 0: return ''
        
        res = ''
        for i in range(len(A[0])):
            char = A[0][i]
            for j in range(1, len(A)):
                if i >= len(A[j]) or char != A[j][i]:
                    return res
            res =  res + char
        return res
        
print Solution().longestCommonPrefix(["abcdefgh", "abefghijk", "abcefgh"])