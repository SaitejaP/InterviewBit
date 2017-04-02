# You are given a string. The only operation allowed is to insert
# characters in the beginning of the string. How many minimum characters
# are needed to be inserted to make the string a palindrome string


class Solution:
    # @param A : string
    # @return an integer

    def solve(self, A):
        lenA = len(A)
        B = A + '\n' + A[::-1]
        i = 1
        j = 0
        lps = [0] * len(B)
        while i < len(B):
            if B[i] == B[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                while j >= 0:
                    j = lps[j - 1]
                    if B[i] == B[j]:
                        j += 1
                        lps[i] = j
                        i += 1
                        break;
                    elif j == 0:
                        lps[i] = 0
                        i += 1
                        break
        return abs(lps[-1] - lenA)

print Solution().solve('aaaaabc')