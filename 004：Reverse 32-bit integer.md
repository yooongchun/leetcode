##Problem Description

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

**示例 1:**

```
输入: 123
输出: 321
```

 **示例 2:**

```
输入: -123
输出: -321
```

**示例 3:**

```
输入: 120
输出: 21
```

**注意:**

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

## Python Solution

使用`pop=x%10 x=x/10 `来进行`pop`操作，`res=res*10+pop`表示`push`操作

```python
class Solution:
    def reverse(self, x: int) -> int:
        res=0
        symbol=1 if x>0 else -1
        while x!=0:
            pop=abs(x)%10
            x=int(x/10)
            res=res*10+pop
            if res>2**31:
                return 0
        return symbol*res
```

## C++ Solution

```c++
static const auto SpeedUp = []{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    return 0;
}();
class Solution {
public:
    int reverse(int x) {
        long ans=0;
        while(x!=0){
            ans=ans*10+x%10;
            x/=10;
        }
        return(ans>INT_MAX ||ans<INT_MIN)?0:ans;
    }
};
```

