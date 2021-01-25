
# 70. 爬楼梯

## 解法

* 方法 1：直接用递归 
* 方法 2：用递归 + 记忆化搜索
* 方法 3：使用动态归化（DP）

[70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)

```
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

```

## 思路分析

* 判断对应的字符串，主要用到了 `%` 求余这个操作符的用法
* 1 到 n 个数字，可以通过一次循环来迭代获取对应的输出字符串
    * 可以先生成 1~n 对应的数组，然后迭代
    * 也可以通过生成

## Python

### 方法 1：直接用递归

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


