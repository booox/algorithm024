# 63. 不同路径 II: 

[63. 不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/)

```
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

示例 1：

输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
示例 2：

输入：obstacleGrid = [[0,1],[0,0]]
输出：1
 

提示：

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] 为 0 或 1
```
## 方法 1: 使用动态规划

### 思路

* 本题是在 [不同路径](code/62-unique-paths.md) 的基础上添加了 **障碍**
* 使用动态规划
    * 

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 1. 使用动态规划，自顶向下
        # 空数组
        if not obstacleGrid:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # 最开始，或最结束点为障碍，返回 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        # 初始值: 全部赋予 0 值
        dp = [[0] * n] * m                 # 通不过 ？？？
        dp = [[0] * n for _ in range(m)]   # 可以
        dp[0][0] = 1 if not obstacleGrid[0][0] else 0

        for row in range(m):
            for col in range(n):
                # 遇到 障碍，则为 0
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                else:
                    # 如果上面可以过来，则加上
                    if row >= 1:   
                        dp[row][col] += dp[row - 1][col]
                    # 如果左边可以过来，则加上
                    if col >= 1:
                        dp[row][col] += dp[row][col - 1]
        return dp[-1][-1]
```

**一个问题：**

下面这两条语句区别在哪里？写成前者通不过，后者却可以？

```python
dp = [[0] * n] * m 
dp = [[0] * n for _ in range(m)]
```


### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()


## 方法 2: 使用深度优先搜索

### 思路

* 

```python

```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()
