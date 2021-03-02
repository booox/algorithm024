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
## 方法 1: 使用动态规划: 自顶向下

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
        # dp = [[0] * n] * m  # 这样为浅复制，不可以
        dp = [[0] * n for _ in range(m)]
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

原因找到了：

* 使用 `[[0] * n] * m` 方式，生成的二维数组，是将 `[0] * n` 这个数组 **复制** 了 `m` 次
    * 被称为 **浅复制** 
* 而使用 `[[0] * n for _ in range(m)]` 方式，则是 **创建** 得到了全新的二维数组。

具体看如下实验

```python
>>> a = [[0] * 3] * 3
>>> a
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> a[0][1] = 1
>>> a
[[0, 1, 0], [0, 1, 0], [0, 1, 0]]   # 每个对应的值对被修改了

>>> b = [[0] * 3 for _ in range(3)]
>>> b
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> b[0][1] = 1
>>> b
[[0, 1, 0], [0, 0, 0], [0, 0, 0]]  # 只修改了 1 个位置

>>> c = [[0 for _ in range(3)] for _ in range(3)]
>>> c
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> c[0][1] = 1
>>> c
[[0, 1, 0], [0, 0, 0], [0, 0, 0]]  # 也是只修改了 1 个位置
```


### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()


## 方法 2: 使用递归深度优先搜索 + lru_cache

### 思路

* 参考 [Python DFS+DP explained solution](https://leetcode.com/problems/unique-paths-ii/discuss/527282/Python-DFS%2BDP-explained-solution)
* 使用递归，从 `(0, 0)` 开始

```python
import functools

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:  # 空数组
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # (0, 0) 或 (m - 1, n - 1) 为障碍
        if obstacleGrid[0][0] or obstacleGrid[m - 1][n - 1]:
            return 0
        
        @functools.lru_cache(None)
        def dfs(row, col):
            # terminator
            if obstacleGrid[row][col]:  # 遇到障碍
                return 0
            if row == m - 1 and col == n - 1:  # 到达 end
                return 1

            count = 0
            # process
            # 向下
            if row < m - 1:
                # drill down
                count += dfs(row + 1, col)
            # 向右
            if col < n - 1:
                # drill down
                count += dfs(row, col + 1)

            return count
            
            # revert states

        return dfs(0, 0)
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()


## 方法 3: 使用递归深度优先搜索 + 缓存

### 思路

* 


**自底向上**

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0

        memo = {}
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        return self.__dfs(obstacleGrid, m - 1, n - 1, memo)

    
    def __dfs(self, grid, row, col, memo):
        # terminator
        if (row, col) in memo:
            return memo[(row, col)]
        # 出界，或遇到障碍
        elif row < 0 or col < 0 or grid[row][col]:
            return 0
        # 到达 start
        elif row == 0 and col == 0:
            return 1

        # process
        # drill down
        # 向上，或向左
        memo[(row, col)] = self.__dfs(grid, row - 1, col, memo) + self.__dfs(grid, row, col - 1, memo)

        return memo[(row, col)]
        # revert states
```


**自顶向下***

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        
        memo = {}
        return self.__dfs(obstacleGrid, 0, 0, memo)

    def __dfs(self, grid, i, j, memo):
        m, n = len(grid), len(grid[0])

        # terminator
        # 缓存
        if (i, j) in memo:
            return memo[(i, j)]
        # 出界，或障碍
        elif i > m - 1 or j > n - 1 or grid[i][j]:
            return 0
        # 到达起点
        elif i == m - 1 and j == n - 1:
            return 1

        # process
        # drill down
        # 向右，向下
        memo[(i, j)] = self.__dfs(grid, i, j + 1, memo) + \
                        self.__dfs(grid, i + 1, j, memo)

        # revert states

        return memo[(i, j)]
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()
