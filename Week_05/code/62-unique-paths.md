# 62. 不同路径: 

[62. 不同路径](https://leetcode-cn.com/problems/unique-paths/)

```
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

 

示例 1：


输入：m = 3, n = 7
输出：28
示例 2：

输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
示例 3：

输入：m = 7, n = 3
输出：28
示例 4：

输入：m = 3, n = 3
输出：6
 

提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 109
```
## 方法 1: 动态规划 - 自底向上递推

### 思路

* 使用动态规划，自顶向后 **递推**
    * 定义 dp[i][j] 为到达 (i, j) 点的有多少中不同的方法
    * 那要怎样到达 (i, j) 点呢？有且只有两种方法：
        * 从上面：(i - 1, j)
        * 从左边：(i, j - 1)
    * 所以，动态转移方程为：
        * dp[i][j] = dp[i - 1][j] + dp[i][j - 1]


```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1

        # 从前往后推， dp[i][j] 表示 到达 (i, j) 点有多少种不同的走法
        # 要到
        dp = [[1] * n] * m
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
```

**双层循环，也可使用 itertools.product**

```python
import itertools
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1

        dp = [[1] * n] * m
        for i, j in itertools.product(range(1, m), range(1, n)):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
```




### 复杂度分析

* 时间复杂度：O(mn)
* 空间复杂度：O(mn)


## 方法 2: 动态规划 - 自顶向下递推

### 思路

* 使用动态规划，自底向上 **递推**
    * 定义 dp[i][j] 为从 (i, j) 点到达 end 有多少中不同的方法
    * 那要怎样才能从 (i, j) 到达 end 呢？有且只有两种方法：
        * 向下：(i + 1, j)
        * 向右：(i, j + 1)
    * 所以，动态转移方程为：
        * dp[i][j] = dp[i + 1][j] + dp[i][j + 1]


```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1

        # 自顶向下：
        # dp[i][j]: 从 (i, j) 到 end 有多少种不同的方法
        dp = [[1] * n] * m
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 or j == n - 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]
```

### 复杂度分析

* 时间复杂度：O(mn)
* 空间复杂度：O(mn)





```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j - 1] + dp[j]
        return dp[-1] if m and n else 0

```