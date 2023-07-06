"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

 
示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1
 

提示：

1 <= nums.length <= 2500
-104 <= nums[i] <= 104

进阶：

你能将算法的时间复杂度降低到 O(n log(n)) 吗?
解：设dp[i]表示[0,i]区间内含nums[i]在内的最大上升序列的长度
则可列出如下状态转移方程：
dp[i] = max(dp[i], dp[j] + 1) for j in [0, i)
"""
from typing import List

class Solution:
    """
    动态规划
    设dp[i]表示以nums[i]结尾的[0,i]区间内的最大上升子序列的长度，
    另设0<=j<i，状态dp[j]到dp[i]满足以下关系：
    1. 当nums[i]>nums[j]，则dp[i] = max(dp[j]+1,dp[i]) for j in [0,i)
    2. 当nums[i]<= nums[j]时，直接跳过
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)


class Solution2:
    """
    贪心匹配+二分查找
    贪心思想：为了使得上升子序列的长度最长，那么每次加入数组的元素应尽可能小。
    然后用target[j]数组记录到j位置的上升序列的最后一个元素
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        target = []
        for i in range(len(nums)):
            # 如果target为空或者当前元素比目标序列的最后一个元素大，则直接插入
            if not target or nums[i] > target[-1]:
                target.append(nums[i])
                continue
            # 如果当前元素等于target最后一个元素，直接跳过
            if nums[i] == target[-1]:
                continue
            # 如果当前元素比target第一个元素还小，直接在target[0]替换
            if nums[i] <= target[0]:
                target[0] = nums[i]
                continue
            # 否则需要查找目标序列中的元素位置
            k = len(target) - 1
            left, mid, right = 0, k//2, k
            while left < mid < right:
                if nums[i] < target[mid]:
                    right = mid
                    mid = (left + mid)//2
                elif nums[i] == target[mid]:
                    break
                else:
                    left = mid
                    mid = (right+mid)//2
            if target[mid] == nums[i]:
                continue
            target[mid+1] = nums[i]
        return len(target)
