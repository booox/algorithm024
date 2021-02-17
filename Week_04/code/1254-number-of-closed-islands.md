# 1254. 统计封闭岛屿的数目: 

[1254. 统计封闭岛屿的数目](https://leetcode-cn.com/problems/number-of-closed-islands/)

```
有一个二维矩阵 grid ，每个位置要么是陆地（记号为 0 ）要么是水域（记号为 1 ）。
我们从一块陆地出发，每次可以往上下左右 4 个方向相邻区域走，能走到的所有陆地区域，我们将其称为一座「岛屿」。
如果一座岛屿 完全 由水域包围，即陆地边缘上下左右所有相邻区域都是水域，那么我们将其称为 「封闭岛屿」。

请返回封闭岛屿的数目。

示例 1：

输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
输出：2
解释：
灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
示例 2：

输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
输出：1
示例 3：

输入：grid = [[1,1,1,1,1,1,1],
             [1,0,0,0,0,0,1],
             [1,0,1,1,1,0,1],
             [1,0,1,0,1,0,1],
             [1,0,1,1,1,0,1],
             [1,0,0,0,0,0,1],
             [1,1,1,1,1,1,1]]
输出：2
 
提示：

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
```
## 方法 1: 使用 DFS 

### 思路

* 借用 [200. 岛屿数量](code/200-number-of-islands.md) 中 DFS 方法
* 不同地方是，需要对「非封装岛屿」进行排除
* 可以添加一个类变量 `self.edged`

```python
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        # 1. use dfs
        # 先按岛屿数量写 dfs，而后再剪枝
        res = 0
        
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    # 遇到新的岛屿，edged 为 False 
                    self.edged = False
                    self.__dfs(grid, i, j, m, n)
                    # 只有当岛屿为「封闭岛屿」才更新结果
                    if not self.edged:
                        res += 1
        return res


    def __dfs(self, grid, i, j, m, n):
        # terminator
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 0:
            return 

        # process
        grid[i][j] = 1

        # 判断 i, j 是否靠边，则 edged 为 True
        if i in {0, m - 1} or j in {0, n - 1}:
            self.edged = True

        # drill down
        self.__dfs(grid, i + 1, j, m, n)
        self.__dfs(grid, i - 1, j, m, n)
        self.__dfs(grid, i, j + 1, m, n)
        self.__dfs(grid, i, j - 1, m, n)



```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()


## 方法 2: 使用 BFS

### 思路

* 与  方法相同
* 不同之外，设置了一个靠边的全局变量 `self.edged` 来判断岛屿是否靠边
* 只要岛屿坐标 `i` 等于 `0` 或 `m - 1`，`j` 等于 `0` 或 `n - 1`，即说明岛屿靠边


```python
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        # 2. use bfs
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    self.edged = False  # 默认非靠边
                    self.__bfs(grid, i, j, m, n)
                    # 如果不靠边，则更新结果
                    if not self.edged:
                        res += 1
        return res

    def __bfs(self, grid, i, j, m, n):
        level = [[i, j]]
        while level:
            i, j = level.pop()
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                grid[i][j] = 1
                level += [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
                # 判断当前岛屿是否靠边
                if i in {0, m - 1} or j in {0, n - 1}:
                    self.edged = True
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()
