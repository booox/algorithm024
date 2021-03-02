# 120. 三角形最小路径和: 

[120. 三角形最小路径和](https://leetcode-cn.com/problems/triangle/)

```
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

 

示例 1：

输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
示例 2：

输入：triangle = [[-10]]
输出：-10
 

提示：

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
```
## 方法 1:  使用动态规划 - top-down

### 思路

* 定义 dp[i][j] 表示 到 (i, j) 元素位置时最小路径和
* 按三角形自顶向下，寻找 **重复性**
    * 到第 1 层，最小路径和即为 **上一层** 的最小路径和，而上面没有层了，所以就为 (0, 0) 元素的值
    * 到第 2 及后面的层，最小路径和就为 **上一层** （第 1 层）的最小路径和，再加上 **当前** 元素值
    * 依次类推
* 但需要注意
    * 在遍历每一层时，要查看是否遍历到了 **左边界** 或 **右边界**

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return

        # use dp - top-down
        dp = [[0 for _ in range(len(row))] for row in triangle ]
        # 要求路径和，所以 dp[0][0] 初始赋值为 triangle[0][0]
        dp[0][0] = triangle[0][0]

        # 因为第一层只有一个，且已经设定好，所以从 2 层开始
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                # 左边界
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j]
                # 右边界
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j])

        return min(dp[-1])
  
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()
