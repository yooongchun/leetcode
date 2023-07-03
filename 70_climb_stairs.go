/*
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
示例 2：

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶

题解：
f(x) = f(x-1) + f(x-2)
*/
package leetcode

import "sync"

var cache map[int]int
var once = sync.Once{}

func climbStairs(n int) int {
	// dp0, dp1 := 1, 1
	// for n >= 2 {
	// 	n -= 1
	// 	dp0, dp1 = dp1, dp0+dp1
	// }
	// return dp1

	once.Do(func() {
		cache = make(map[int]int)
	})

	// method 2
	if n <= 1 {
		return 1
	}
	if _, ok := cache[n-1]; !ok {
		cache[n-1] = climbStairs(n - 1)
	}
	if _, ok := cache[n-2]; !ok {
		cache[n-2] = climbStairs(n - 2)
	}

	return cache[n-1] + cache[n-2]
}
