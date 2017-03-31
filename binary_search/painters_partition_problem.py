# encoding=utf8
# You have to paint N boards of length {A0, A1, A2, A3 … AN-1}. There are
# K painters available and you are also given how much time a painter
# takes to paint 1 unit of board. You have to get this job done as soon as
# possible under the constraints that any painter will only paint
# contiguous sections of board.


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer

    def paint(self, A, B, C):
        low = max(C) * B
        high = sum(C) * B
        while low < high:
            mid = (low + high) / 2
            if self.isPossible(A, B, C, mid):
                high = mid
            else:
                low = mid + 1
        return low % 10000003

    def isPossible(self, A, B, C, n):
        work_done = [0] * A
        i = 0
        n_worker = 0
        while i < len(C):
            work_inc_curr_board = work_done[n_worker] + B * C[i]
            if work_inc_curr_board > n:
                n_worker += 1
            if n_worker == A:
                return  False
            work_done[n_worker] += B * C[i]
            i += 1
        return True

print Solution().paint(1, 1000000, [1000000, 1000000])
