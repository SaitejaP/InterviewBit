# N number of books are given. The ith book has Pi number of pages. You
# have to allocate books to M number of students so that maximum number of
# pages alloted to a student is minimum. A book will be allocated to
# exactly one student. Each student has to be allocated at least one book.
# Allotment should be in contiguous order, for example: A student cannot
# be allocated book 1 and book 3, skipping book 2.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def books(self, A, B):
        if len(A) < B:
            return -1
        elif len(A) == B:
            return max(A)
        else:
            low = max(A)
            high = sum(A)
            while low < high:
                mid = (low + high) / 2
                req = self.reqStudents(A, mid)
                if B >= req:
                    high = mid
                else:
                    low = mid + 1

            return low

    def reqStudents(self, A, mid):
        total = 0
        numStudents = 1
        for i in range(len(A)):
            if total + A[i] > mid:
                numStudents += 1
                total = A[i]
            else:
                total += A[i]
        return numStudents

print Solution().books([12, 34, 67, 90], 2)