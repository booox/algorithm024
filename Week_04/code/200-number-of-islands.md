# 200. 岛屿数量: 

[200. 岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)

```
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'    
```

## 方法 1: 使用 DFS 

### 思路

* 对二维网络进行双层循环遍历
    * 当遇到某一点 `grid[i][j] == "1"` 时，岛屿计数加 1
    * 并从该点「上下左右」用 `dfs` 递归，将相邻的 `1` 均变成 `0`
* `dfs` 函数
    * 从点 `(i, j)` 向四周「上下左右」探索
    * 终止条件：越界，或遇到某一点 `grid[i][j] != "1"` 中止
    * 执行操作：将 `grid[i][j] = "0"`，这样就不会被重复计数了


```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        # 对 grid 进行遍历
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    self.__dfs(grid, i, j, m, n)
        return res


    def __dfs(self, grid, i, j, m, n):
        # terminator
        # 超出 grid 边界停止；遇到 0 返回
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != "1":
            return

        # process
        grid[i][j] = "0"

        # drill down
        # 朝当前坐标的「上下左右」四个方向搜索
        self.__dfs(grid, i + 1, j, m, n)
        self.__dfs(grid, i - 1, j, m, n)
        self.__dfs(grid, i, j + 1, m, n)
        self.__dfs(grid, i, j - 1, m, n)

        # revert states
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()


## 方法 2: 使用 BFS

### 思路

* 主体循环与 方法 1 类似
* `bfs` 函数
    * 将给定的点 `(i, j)` 压入待搜索列表 `level` 中
    * 当 `level` 非空时执行下面循环
        * 从 `level` 中弹出末尾坐标
        * 判断是否在界内并且对应值为 "1"
        * 若是，则将对应值修改为 "0"
        * 并将与之相邻的点，压入 `level` 中等待下一步搜索

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 2. use bfs
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    self.__bfs(grid, i, j, m, n)
        return res

    def __bfs(self, grid, i, j, m, n):
        level = [[i, j]]
        while level:
            i, j = level.pop()
            if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                grid[i][j] = "0"
                level += [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()

