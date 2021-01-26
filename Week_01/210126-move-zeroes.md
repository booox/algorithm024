
# 283. 移动零

[283. 移动零](https://leetcode-cn.com/problems/move-zeroes/)

## 解法

* 使用双指针


```
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
```

## 思路分析



## Python

### 方法 1：双指针

#### 思路

* 

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # 1. use recursive
        # # timeout
        def worker(x):
            if x == 1 or x == 2:
                return x
            return worker(x - 1) + worker(x - 2)

        return worker(n)
```

> 上述代码提交会超时，因为在递归过程中会出现太多的重复计算

#### 复杂度分析

* 时间复杂度：O(n)  （？）
* 空间复杂度：O(1)

### 方法 2：用递归 + 记忆化搜索

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # 2. use recursive & memo search
        def worker(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = worker(x - 1) + worker(x - 2)

            return memo[x]
        
        memo = {1: 1, 2: 2}
        return worker(n)
```


#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(n)

### 方法 3：使用动态归化（DP）

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # 3. use dp
        memo = {1: 1, 2: 2}

        if n in memo:
            return memo[n]

        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[n]
```


#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(n)


