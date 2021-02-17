# 695. 岛屿的最大面积: 

[695. 岛屿的最大面积](https://leetcode-cn.com/problems/max-area-of-island/)

```
给定一个包含了一些 0 和 1 的非空二维数组 grid 。

一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

注意: 给定的矩阵grid 的长度和宽度都不超过 50。

```
## 方法 1: 使用 DFS

### 思路

* 借用 [200. 岛屿数量](code/200-number-of-islands.md) 中 DFS 方法
    * 对 grid 遍历
        * 遇到为 `1` 的地方，从这里下探到四周相邻地方，并将相邻也为 `1` 的变成 `0`
        * 同时记录 `1` 的个数


```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        # 1. use dfs
        # 遍历 grid，遇到 1，递归扫描
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(self.__dfs(grid, i, j, m, n), res)
        return res

    
    def __dfs(self, grid, i, j, m, n):
        # terminator
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
            return 0

        # process
        maxv = 1
        grid[i][j] = 0

        # drill down
        maxv += self.__dfs(grid, i + 1, j, m, n)
        maxv += self.__dfs(grid, i - 1, j, m, n)
        maxv += self.__dfs(grid, i, j + 1, m, n)
        maxv += self.__dfs(grid, i, j - 1, m, n)
        # revert states

        return maxv
```

* 本题调试时出现两个错误：
    * 没有注意审题，将本题中的 `1` 与 `0` 自以为与 **200** 题一样，都为 `"1"` 与 `"0"`
        * 这里耽误了好一会。
    * 将 `grid[i][j] = 0` 写成 `grid[i][j] == 0`，造成了递归层数太多
        * 也是耽搁了好一会

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()



## 方法 2: 使用 BFS

### 思路

* 借用 [200. 岛屿数量](code/200-number-of-islands.md)中 BFS 方法
* 不同的地方就是
    * 在 bfs 中需要记录当前岛屿的大小

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 2. use bfs
        if not grid:
            return 0

        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, self.__bfs(grid, i, j, m, n))

        return res

    def __bfs(self, grid, i, j, m, n):
        level = [[i, j]]
        maxv = 0
        while level:
            i, j = level.pop()
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 0
                maxv += 1
                level += [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
        return maxv

```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()
