# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).

class Solution:
    # @param A : list of list of integers
    # @return the same list modified

    def rotate(self, A):
        if len(A) == 1:
            return A

        n = len(A)

        for i in range(n / 2):
            left = i
            right = n - 1 - i
            top = i
            bottom = n - 1 - i
            for j in range(right - left):
                temp = A[top][left + j]
                A[top][left + j] = A[bottom - j][left]
                A[bottom - j][left] = A[bottom][right - j]
                A[bottom][right - j] = A[top + j][right]
                A[top + j][right] = temp
        return A


mat = [[27, 35, 36, 47, 94, 133, 163, 164, 235, 253, 280, 310, 339, 352], [46, 72, 77, 95, 144, 149, 158, 174, 242, 243, 317, 371, 378, 386], [13, 14, 80, 83, 121, 157, 158, 163, 215, 220, 308, 325, 388, 397], [11, 38, 45, 84, 105, 132, 134, 145, 184, 219, 282, 298, 380, 381], [23, 27, 42, 118, 120, 139, 168, 225, 243, 271, 274, 349, 393, 395], [22, 27, 49, 85, 103, 167, 175, 234, 241, 258, 283, 296, 352, 385], [24, 78, 117, 119, 137, 147, 173, 189, 193, 216, 281, 304, 332, 358], [
    27, 71, 108, 109, 112, 133, 137, 145, 150, 171, 195, 225, 260, 336], [5, 56, 65, 114, 123, 200, 220, 222, 248, 264, 285, 317, 350, 367], [2, 20, 60, 72, 75, 130, 136, 149, 189, 254, 264, 295, 315, 349], [23, 35, 68, 77, 104, 129, 153, 165, 248, 253, 290, 316, 321, 394], [34, 127, 129, 154, 186, 202, 203, 210, 235, 269, 331, 344, 376, 387], [11, 98, 99, 118, 119, 183, 250, 252, 277, 280, 291, 307, 360, 368], [42, 74, 93, 119, 178, 186, 198, 221, 234, 295, 296, 319, 322, 335]]
print Solution().rotate(mat)
