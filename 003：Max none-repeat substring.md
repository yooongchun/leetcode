## Information

[![author-info](https://img.shields.io/badge/Author-yooongchun-yellowgreen.svg)](http://www.yooongchun.com) [![](https://img.shields.io/badge/Email-yooongchun%40foxmail.com-brightgreen.svg)]() [![](https://img.shields.io/badge/Wechat-18217235290-blue.svg)]() ![wechatOfficialAccount](https://img.shields.io/badge/WechatOfficialAccount-yooongchuncabin-yellow.svg) 

[![](https://fanyuzone.oss-cn-beijing.aliyuncs.com/image/WechatOfficialAccount_small.jpg)]()

## Problem Description

给定一个字符串，请你找出其中不含有重复字符的 **最长子串** 的长度。

**示例 1:**

```
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

**示例 2:**

```
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```

**示例 3:**

```
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

## Problem Solving

记录重复出现的位置，每当重复则删除数组重复位置之前的部分。

## Python solution

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        list_=[]
        max_=0
        for c in s:
            if c in list_:del list_[0:list_.index(c)+1]
            list_.append(c)
            max_=len(list_) if len(list_)>max_ else max_
        return max_
```

## C++ solution

- 使用两个指针记录当前最大不重复序列，遍历序列不断修改指针。同时，用`max_`记录每次循环的最大不重复值。

- 求`string` 的子串函数

  ```c++
  string::size_type substr(int pos,int len);
  ```

- 求`string`中子串的位置

  ```c++
  s.find(substring);    
  ```

- 使用s.npos判断是否找到

  ```c++
  s.find(substring)==s.npos
  ```

  ```c++
  class Solution
  {
    public:
      int lengthOfLongestSubstring(string s)
      {
          if (s.size() <= 1)
              return s.size();
  
          int max_ = 1;
          int i = 0, j = 1;
          for (j = 1; j < s.size(); j++)
          {
              string sub = s.substr(i, j-i);
              int pos = sub.find(s[j]);
              if (pos != sub.npos)
                  i += pos + 1;
              else if (1 + j - i > max_)
                  max_ = 1 + j - i;
          }
          return max_;
      }
  };
  ```


- 使用哈希映射。使用长度为128的数组映射字母及其位置关系

- 使用`ios::sync_with_stdio(false)`来解除`std::cin` 和`std::cout` 与`stdio`中输入输出的同步；使用`cin.tie(nullptr)` 来解除输入输出的绑定；以上两个操作节约运行时间。

  ```c++
  static int x = [](){ios::sync_with_stdio(false); cin.tie(nullptr); return 0; }();
  class Solution {
  public:
      int lengthOfLongestSubstring(string s) {
          vector <int>hax(128,-1);
          int res=0;
          int left=-1;
          for(int i=0;i<s.size();++i)
          {
              left=max(left,hax[s[i]]);
              hax[s[i]]=i;
              res=max(i-left,res);
          }
          return res;
      }
  };
  ```


