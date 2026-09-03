# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 请必须使用时间复杂度为 O(log n) 的算法。
# 从标准库 `typing` 导入 `List`，用来做**类型注解**，只给人 / IDE 看，不影响程序运行。

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # 去除数据长度
        low = 0
        high = len(nums) - 1
        hit = 0
        while low <= high:
            mid = (low + high) // 2

            # 判断目标值是否大于中位数
            if target < nums[mid]:
                high = mid - 1
                hit = high + 1
            elif target > nums[mid]:
                low = mid + 1
                hit = low
            else:
                hit = mid
                break

        if hit < 0:
            hit = 0

        return hit


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchInsert([1, 3], 2))
