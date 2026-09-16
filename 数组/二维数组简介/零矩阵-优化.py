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

核心思想：复用矩阵首行首列做标记，空间 O (1)

实际应用场景：图像处理（图像像素矩阵） 例如：二值图像，找到所有黑点，把黑点所在整行、整列涂黑。 内存不足的图像算法（移动端 / 边缘相机）

原地标记主要用于内存受限场景，比如嵌入式传感器矩阵、边缘设备图像处理。核心是避免额外分配数组，降低内存开销。
但业务开发一般不会这么写，因为会修改原始数据，可读性差，调试困难。
只有资源受限的底层场景，才会牺牲可读性换取内存节省。
'''

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        矩阵置零：原地修改，如果某个元素为0，则它所在整行、整列全部置0
        思路：复用矩阵第0行、第0列作为标记数组，减少额外空间
        """
        m, n = len(matrix), len(matrix[0])

        # flag_col0：记录【原始第0列】是否存在0
        flag_col0 = any(matrix[i][0] == 0 for i in range(m))
        # flag_row0：记录【原始第0行】是否存在0
        flag_row0 = any(matrix[0][j] == 0 for j in range(n))

        # ========== 【打标记阶段】你刚才问的这段代码 ==========
        # 跳过第0行和第0列，遍历矩阵内部所有元素
        for i in range(1, m):
            for j in range(1, n):
                # 如果当前位置是0
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # 在本行第0列打标记：第i行需要全部置0
                    matrix[0][j] = 0  # 在本列第0行打标记：第j列需要全部置0

        # ========== 【根据标记置零阶段】 ==========
        # 再次遍历内部元素，查看标记，满足条件就置0
        for i in range(1, m):
            for j in range(1, n):
                # 本行标记为0 OR 本列标记为0 → 当前位置置0
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # ========== 单独处理第0列、第0行 ==========
        # 如果原始第0列有0，则把整列置0
        if flag_col0:
            for i in range(m):
                matrix[i][0] = 0
        # 如果原始第0行有0，则把整行置0
        if flag_row0:
            for j in range(n):
                matrix[0][j] = 0

        print(matrix)

if __name__ == "__main__":
    matrix = [[1, 2, 3, 4, 0], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
    Solution().setZeroes(matrix)
