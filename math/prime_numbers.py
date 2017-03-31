# Given a number N, find all prime numbers upto N ( N included ).

class Solution:
    # @param A : integer
    # @return a list of integers

    def sieve(self, A):
        if A < 2:
            return []

        div = [0] * (A + 1)
        ans = []
        for i in range(2, A + 1):
            if div[i] == 0:
                ans.append(i)
                j = i * 2
                while j <= A:
                    div[j] = 1
                    j += i
        return ans

print Solution().sieve(17)