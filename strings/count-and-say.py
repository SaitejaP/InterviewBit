# The count-and-say sequence is the sequence of integers beginning as
# follows: 1, 11, 21, 1211, 111221, .... Given an integer n, generate the
# nth sequence.


class Solution:
    # @param A : integer
    # @return a strings

    def countAndSay(self, A):
        if A == 1:
            return '1'
        if A == 2:
            return '11'

        start = '11'
        for j in range(2, A):
            prev = start[0]
            count = 1
            _next = ''
            for i in range(1, len(start)):
                if prev == start[i]:
                    count += 1
                else:
                    _next = '%s%s%s' % (_next, count, prev)
                    prev = start[i]
                    count = 1
            start = '%s%s%s' % (_next, count, prev)
        return start

print Solution().countAndSay(10)