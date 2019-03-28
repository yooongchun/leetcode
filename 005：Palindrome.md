## Problem Description

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

**示例 1:**

```
输入: 121
输出: true
```

**示例 2:**

```
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
```

**示例 3:**

```
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
```

**进阶:**

你能不将整数转为字符串来解决这个问题吗？

## Python Solution

使用整数反转：

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev=0
        num=x
        while num!=0:
            rev=rev*10+num%10
            num=int(num/10)
        if rev==x:
            return True
        else:
            return False
```

反转一半整数：

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x<10:
            return True
        if x%10==0:
            return False
        rev=0
        num=x
        while True:
            rev=rev*10+num%10
            num=int(num/10)
            if rev==num or rev==int(num/10):
               return True 
            if rev>num:
                return False
```

转为字符串反转字符串：

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
```

## C++ Solution

整数反转：

```c++
static int x = []() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	return 0;
}();
class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0) return false;
        if(x<10)return true;
        if(x%10==0)return false;
        int rev=0;
        while(1){
            rev=rev*10+x%10;
            x/=10;
            if(rev==x||rev==x/10)return true;
            if(rev>x)return false;
        }
    }
};
```

字符串反转：

```c++
static int x = []() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	return 0;
}();
class Solution {
public:
    bool isPalindrome(int x) {
        string rev=to_string(x);
        reverse(rev.begin(),rev.end());
        return rev==to_string(x);
        }
};
```

## 算法复杂度分析

- 时间复杂度：$O(log_{10}(n))$
- 空间复杂度：$O(1)$

