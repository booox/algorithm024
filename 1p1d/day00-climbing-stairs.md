
# Day01: 70. 爬楼梯

[70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)

## 解法

* 方法 1：直接用递归 
* 方法 2：用递归 + 记忆化搜索
* 方法 3：使用动态归化（DP）


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

* 楼梯只有 1 阶，则有 1 种走法；2 阶楼梯，则有1 阶 1 阶走两次，和一次性跨到 2 阶两种方法
* 要求 n 阶楼梯走法，如果能告诉我第 n - 1 阶和 n - 2 阶 **分别** 有几种走法，将二者相加起来，即为所求。
* 可以使用递归，但要注意使用记忆化搜索，来消除重复的计算
* 也可以使用动态规划

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


