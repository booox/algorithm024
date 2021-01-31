# 11. 盛最多水的容器

[11. 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/)

```
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。

示例 1：

输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1
示例 3：

输入：height = [4,3,2,1,4]
输出：16
示例 4：

输入：height = [1,2,1]
输出：2

```
## Python

### 方法 1: 暴力解法

#### 思路

* 双层循环
    * 外层循环 i: (0, n-2)
    * 内层循环 j: i + 1, n - 1
    * 得到当前组成面积
* 将当前的面积与前面的最大面积比较，取较大者

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 1. 使用暴力
        maxarea, size = 0, len(height)

        for i in range(size-1):
            for j in range(i+1, size):
                area = (j - i) * min(height[i], height[j])
                maxarea = max(area, maxarea)
        return maxarea
```

#### 复杂度分析

* 时间复杂度：O(n^2)
* 空间复杂度：O(1)


### 方法 2: 双打针：左右撞针

#### 思路

* 从左右两端向中间收敛
    * 比较两端元素大小，较小侧向内移动一个元素
    * 同时比较当前面积，与此前最大面积

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 2. 双指针：左右撞针
        i, j = 0, len(height) - 1
        maxarea = 0

        while i < j:
            area = (j - i) * min(height[i], height[j])
            maxarea = max(maxarea, area)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

        return maxarea
```

#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(1)

