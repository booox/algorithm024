# 64. 最小路径和: 

[64. 最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)

```
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

 

示例 1：


输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
```
## 方法 1: 动态规划：自顶向下

### 思路

* 要求 **路径上的数字总和为最小**
* 使用 **自顶向下** 的方法
* 定义 `dp[i][j]`，表示到 (i, j) 点时，最小的数字总和
* 因为 **每次只能向下或者向右移动一步**，那对 (i, j) 点来说
    * `dp[i][j]到该点的路径最小数字和 = grid[i][j] + min(左边数字和, 上边数字和)`
* 有两个特殊情况需要考虑：
    * 当 `(i, j)` 在第 1 行时，因为上面没有格子了，**最小**只能是 `dp[i][j - 1] + grid[i][j]`
    * 当 `(i, j)` 在第 1 列时，因为左边没有格子了，**最小**只能是 `dp[i - 1][j] + grid[i][j]`



```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        if m == n == 1:
            return grid[0][0]

        # use dp
        # dp[i][j]: 到达 (i, j) 点，路径上数字之和最小值
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        # 遍历
        for i in range(m):
            for j in range(n):
                if i == 0:    # 在第 1 行
                    dp[i][j] = grid[i][j] + dp[i][j - 1] 
                elif j == 0:  # 在第 1 列
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                else:         # other
                    dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
```

### 复杂度分析

* 时间复杂度：O(mn)
    * 需要对每个格子遍历一次，计算 dp 的值
* 空间复杂度：O(mn)
    * 需要存储 m * n 个值


## 方法 2: 动态规划：自底向上

### 思路

* 思路与方法 1 相同，只是此时使用 **自底向上** 
* 定义 `dp[i][j]`，表示从 (i, j) 点到终点最小的数字总和
* 因为 **每次只能向下或者向右移动一步**，那对 (i, j) 点来说
    * `从 (i, j) 点到终点的路径最小数字和 = grid[i][j] + min(右边数字和, 下边数字和)` 
* 同样需要考虑两种特殊情况：
    * 最后一行，因为下面没有格子，只能向右，所以最小值为：`grid[i][j] + dp[i][j + 1]`
    * 最后一列，因为右面没有格子，只能向下，所以最小值为：`grid[i][j] + dp[i + 1][j]`

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        # use dp
        # dp[i][j]: 从 (i, j) 点到 end 路径上数字之和最小值
        dp = [[0] * n for _ in range(m)]
        dp[-1][-1] = grid[-1][-1]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # print()
                if i == m - 1 and j != n - 1:    # 最后一行，只能向右
                    dp[i][j] = grid[i][j] + dp[i][j + 1]
                elif j == n - 1 and i != m - 1:  # 最后一列，只能向上
                    dp[i][j] = grid[i][j] + dp[i + 1][j]
                elif i != m - 1 and j != n - 1:
                    dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
                    
        return dp[0][0]

```

### 复杂度分析

* 时间复杂度：O(mn)
    * 需要对每个格子遍历一次，计算 dp 值
* 空间复杂度：O(mn)
    * 需要存储 m * n 个值


## 方法 3: 动态规划: 压缩空间

### 思路

* 空间复杂度可以优化，例如每次只存储上一行的 dp 值，则可以将空间复杂度优化到 O(n)。
* 根据 **前一行的值** 来计算 **当前行**
* 注意将初始值设定为 `float('inf')`
* 注意在每一行遍历时，如何初始化 `dp[0]`
* 参考： [Python Solution with Detailed Explanation](https://leetcode.com/problems/minimum-path-sum/discuss/23532/Python-Solution-with-Detailed-Explanation)

```python

```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()
