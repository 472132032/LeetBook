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


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 排序：按区间起点升序排列，这样重叠的区间就会相邻
        intervals.sort(key=lambda x: x[0])

        new_interval = intervals[0]
        new_intervals = [new_interval]
        # 合并：遍历排序后的区间，若当前区间起点 ≤ 上一个区间的终点，则合并；否则加入结果
        for interval in intervals[1:]:
            if interval[0] <= new_interval[1]:
                if interval[1] > new_interval[1]:
                    new_interval[1] = interval[1]
            else:
                new_interval = interval
                new_intervals.append(interval)

        return new_intervals


if __name__ == "__main__":
    solution = Solution()
    intervals = [[2, 6], [1, 4], [8, 10], [15, 18]]
    print(solution.merge(intervals))
