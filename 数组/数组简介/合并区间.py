# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间
#
#
# 示例 1：
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
# 示例 2：
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
#
# 示例 3：
# 输入：intervals = [[4,7],[1,4]]
# 输出：[[1,7]]
# 解释：区间 [1,4] 和 [4,7] 可被视为重叠区间。
# 现在看AI解释更香了
# 合并区间的核心思想是先排序，再合并：
# 排序：按区间起点升序排列，这样重叠的区间就会相邻
# 合并：遍历排序后的区间，若当前区间起点 ≤ 上一个区间的终点，则合并；否则加入结果

from typing import List


## 冒泡排序区间
def bubble_sort(intervals: List[List[int]]):
    length = len(intervals)

    flag = True

    # 外层是冒泡的次数
    for i in range(length):

        # 判断当前元素是否升序
        flag = True

        # 完成一轮排序
        for j in range(length - i - 1):

            # 两两比较来升序
            if intervals[j][0] > intervals[j + 1][0]:
                tmp = intervals[j]
                intervals[j] = intervals[j + 1]
                intervals[j + 1] = tmp
                # 发生交换就说明当前不符合升序，就是说明发生了交换
                flag = False

        if flag:
            return intervals

    return intervals


# 合并重叠
def merge_cross(intervals: List[List[int]]) -> List[List[int]]:
    new_intervals = list()
    mark = 0
    skip = 0

    # 起点断点放入
    new_interval = intervals[0]

    new_intervals.append(new_interval)

    for i in range(len(intervals)):

        # 相交
        if new_intervals[mark][1] > intervals[i][0]:
            # 第一段是不是包含第二个区间
            if new_intervals[mark][1] < intervals[i][1]:
                new_intervals[mark][1] = intervals[i][1]
            # 其他情况不做处理

        # 起点和终点一样
        elif new_intervals[mark][1] == intervals[i][0]:
            new_intervals[mark][1] = intervals[i][1]

        # 不相交
        else:
            new_intervals.append(intervals[i])
            mark += 1

    return new_intervals


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 对区间起点进行冒泡排序保证起点全局有序
        new_intervals = bubble_sort(intervals)


        # 合并相交
        return merge_cross(new_intervals)


if __name__ == "__main__":
    solution = Solution()
    intervals = [[2, 6], [1, 4], [8, 10], [15, 18]]
    print(solution.merge(intervals))
