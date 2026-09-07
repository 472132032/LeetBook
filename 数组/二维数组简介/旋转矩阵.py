# 给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。

# 不占用额外内存空间能否做到？
#
#  
#
# 示例 1：
#
# 给定 matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
#
# ‌90 度顺时针‌：新位置 (i,j) 的元素来自原位置 (n-j-1, i)，其中 n 为矩阵行数。
# ‌180 度旋转‌：元素位置变为 (n-i-1, n-j-1)，相当于上下翻转后再左右翻转。
# ‌270 度顺时针‌：等同于逆时针旋转 90 度，新位置 (i,j) 的元素来自原位置 (j, n-i-1)。

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 矩阵的行数
        n = len(matrix)

        for matrix1 in matrix:
            for i in range(len(matrix1)) :
                matrix1[i] = matrix1[i-1]


if __name__ == "__main__":
    matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
    Solution().rotate(matrix)
