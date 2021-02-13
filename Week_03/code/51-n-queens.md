# 51. N 皇后: 

[51. N 皇后](https://leetcode-cn.com/problems/n-queens/)

```
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

 

示例 1：


输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：

输入：n = 1
输出：[["Q"]]
 

提示：

1 <= n <= 9
皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
```
## Python

### 方法 1: 回溯算法

#### 思路

* 这里也是排列组合，要首先想到用「回溯」算法，进行深度优先搜索
* 使用三个集合记录 cols, pie, na 记录每一列，两个方向的对角线（撇、捺）位置
* 代码实现上：
    * 也是采用「自顶向下」方法，这样整体思路比较清晰，易阅读，易扩展
    * 在写 dfs 时，先把模板列出，再考虑实现细节


```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:
            return []

        res = []  # 结果集
        # 保存皇后已存在的位置：列、撇、捺 （后两个为对角线）
        self.cols, self.pie, self.na = set(), set(), set()
        self.dfs(n, 0, [], res)
        return self._generate_result(n, res)  # 生成最终输出结果

    def dfs(self, n, row, path, res):
        # terminator
        if row == n:
            res.append(path)
            return

        # process
        # current level, Do it!
        for col in range(n):
            # 剪枝
            if (col in self.cols) or (row + col in self.pie) or (row - col in self.na):
                continue

            # 找到合适位置
            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)

            # drill down
            self.dfs(n, row + 1, path + [col], res)

            # revert states
            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)            


    def _generate_result(self, n, res):
        board = []
        for r in res:
            for i in r:
                board.append("." * i + "Q" + "." * (n - 1 - i))
        return [board[i: i + n] for i in range(0, len(board), n)]

        # 也可直接简写为：
        # return [ ["." * i + "Q" + "." * (n - 1 - i) for i in r] for r in res ]
```

#### 复杂度分析

* 时间复杂度：O(n^2)
* 空间复杂度：O(n)


### 方法 2: 同上，但代码很简洁

#### 思路

* 思路同上，但更简洁

```python
def solveNQueens(self, n):
    def DFS(queens, xy_dif, xy_sum):
        """
        :params queens: 皇后所在的列
        :params xy_dif: 行列之差，向左下的对角线
        :params xy_sum: 行列之和，向右上的对角线
        """
        p = len(queens)
        # 如果长度为 n，并添加到结果集中
        if p==n:
            result.append(queens)
            return None

        # 对每一列处理
        for q in range(n):
            # 如果当前列不在已经产生的列、两条对角线集合内，则向下一层搜索
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
    result = []
    DFS([],[],[])

    # 使用列表的理解生成最终的结果
    return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
```

#### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()


### 方法 3: 思路同上，将生成棋盘的过程在递归时就完成

#### 思路

* 将生成棋盘的过程，直接在将分步结果添加到结果集时就完成
    * 好处：代码更简洁了一些
    * 缺点：如果想对生成棋盘进行更多的变化，原有的代码扩展性就差了


```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:
            return []

        # 保存皇后所在的列、两条对角线
        self.cols, self.pie, self.na = set(), set(), set()
        res = []
        self.dfs(n, 0, [], res)
        return res
        # return self._generate_result(n, res)

    def dfs(self, n, row, path, res):
        # terminator
        if row == n:
            # res.append(path[:])
            # 直接在这里将最终结果
            res.append( [ "." * i + "Q" + "." * (n - 1 - i) for i in path] )
            return

        # process
        for col in range(n):
            # prunning
            if (col in self.cols) or (row + col in self.pie) or (row - col in self.na):
                continue
            
            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)

            # drill down
            self.dfs(n, row + 1, path + [col], res)

            # revert states
            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)


    # def _generate_result(self, n, res):
    #     return [ [ "." * i + "Q" + "." * (n - 1 - i) for i in r] for r in res]


```

#### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()

