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
        
        # 取最后一行的最小值
        return min(dp[-1])
  
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()


## 方法 2: 动态规划-top-down，原地修改

### 思路

* 思路同方法 1，只是这次没有额外创建二维数组，而是选择修改原有的数组

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return

        # 动态规划：top-down，原地修改
        # 参考国际站题解
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                # 左边界
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                # 右边界
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                # other
                else:
                    triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
        return min(triangle[-1])
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()


## 方法 3: 动态规划，bottom-up，一维 dp 数组

### 思路

* 先初始化一维数组 dp 为 triangle 的最后一行
* dp[i] 表示从某一行的第 i 个索引位置到最后一行元素的 **最小路径和**
* 则从倒数第 2 行开始看起，从左往右遍历
    * dp[i] 等于 当前位置元素的值 + min(下一行 i 位置的 dp，下一行 i + 1 位置的 dp)
* 注意遍历的起始位置
    * 外层循环从倒数第 2 行开始，内层循环从左到右依次遍历当前行所有元素。
* 最后 `dp` 长度虽然还是最后一行的长度，但到最上面一行，变化的就只是最前面的那个元素了。此时返回的就应该是 `dp[0]`。

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return

        # 动态规划：bottom - up，额外数组
        # 使 dp 数组初始化为倒数最后一行
        dp = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # 更新 dp，等于 当前值 + min(下一行左)
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
                
        return dp[0]
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()



## 方法 4: 动态规划：bottom-up，原地修改

### 思路

```
   2
  3 4
 6 5 7
4 1 8 3
```

* 遍历从倒数第 2 行到第 0 行，同时遍历每行元素
* 直接修改原二维数组
    * 更新后的值 = 原来的值 + min(下一行左边值，下一行右边值)
* 直到最后，返回 (0, 0) 元素

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return

        # 3. 动态规划：bottom - up
        # 原地修改
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()

