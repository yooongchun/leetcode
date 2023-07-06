/*
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
*/

/*
动态规划
设dp[i]表示以nums[i]结尾的[0,i]区间内的最大上升子序列的长度，
另设0<=j<i，状态dp[j]到dp[i]满足以下关系：
1. 当nums[i]>nums[j]，则dp[i] = max(dp[j]+1,dp[i]) for j in [0,i)
2. 当nums[i]<= nums[j]时，直接跳过
*/
package leetcode

func lengthOfLIS(nums []int) int {
	// 初始化 dp 数组
	dp := make([]int, len(nums))
	for i := 0; i < len(nums); i++ {
		dp[i] = 1
	}
	// 状态方程
	for i := 0; i < len(nums); i++ {
		for j := 0; j < i; j++ {
			if nums[j] < nums[i] && dp[i] < dp[j] {
				dp[i] = dp[j] + 1
			}
		}
	}
	// 取最大值返回
	maxVal := dp[0]
	for _, val := range dp {
		if maxVal < val {
			maxVal = val
		}
	}
	return maxVal
}

/*
贪心匹配+二分查找
贪心思想：为了使得上升子序列的长度最长，那么每次加入数组的元素应尽可能小。
然后用target[j]数组记录到j位置的上升序列的最后一个元素
*/
func lengthOfLIS2(nums []int) int {
	target := []int{}
	for i := 0; i < len(nums); i++ {
		n := len(target)
		// 空列表或者当前元素大于target最后一个元素，直接追加元素
		if n == 0 || target[n-1] < nums[i] {
			target = append(target, nums[i])
			continue
		}
		// 当前元素等于target最后一个元素，跳过
		if target[n-1] == nums[i] {
			continue
		}
		// 当前元素小于等于target第一个元素，则覆盖
		if target[0] >= nums[i] {
			target[0] = nums[i]
			continue
		}
		// 否则二分搜索查找元素插入位置
		left, right, mid := 0, n-1, (n-1)/2
		for left < mid && right > mid {
			if nums[i] < target[mid] {
				right = mid
				mid = (left + mid) / 2
			} else if nums[i] == target[mid] {
				break
			} else {
				left = mid
				mid = (mid + right) / 2
			}
		}
		// 如果是元素相等的情况，直接跳过
		if nums[i] == target[mid] {
			continue
		}
		// 否则直接插入
		target[mid+1] = nums[i]
	}
	return len(target)
}
