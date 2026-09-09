'''
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。


示例 1：

输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2：

输入：
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出：
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]


'''
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 行
        row = []
        # 列
        col = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)

        row = set(row)
        col = set(col)

        # 行弄成0
        for i in range(len(matrix)):
            if i not in row:
                continue
            for j in range(len(matrix[i])):
                matrix[i][j] = 0

        # 列弄成0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j in col:
                    matrix[i][j] = 0

        print(matrix)


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4, 0], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
    Solution().setZeroes(matrix)
