# 239. 滑动窗口最大值: 

[239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)

```
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

 

示例 1：

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
示例 2：

输入：nums = [1], k = 1
输出：[1]
示例 3：

输入：nums = [1,-1], k = 1
输出：[1,-1]
示例 4：

输入：nums = [9,11], k = 2
输出：[11]
示例 5：

输入：nums = [4,-2], k = 2
输出：[4]
 

提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
```
## Python

### 方法 1: 暴力（会超时）

#### 思路

* 遍历 0, len(nums) - k，用数组切片直接获取每个窗口的最大值，并加入到结果集当中。

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # # 1. 暴力解法 (timeout)
        # # i -> (0, n - k)
        if len(nums) <= 1 or k == 1:
            return nums

        res = []
        for i in range(len(nums) - k + 1):
            maxv = max(nums[i: (i + k)])
            res.append(maxv)

        return res
```

#### 复杂度分析

* 时间复杂度：O(n * O(max))
* 空间复杂度：O()

### 方法 2: 使用单调的双向队列 (use list)

#### 思路

* 使用双向队列，最左为最大，自左向右依次减小
* 队列中存储的是元素的索引，不是元素的值

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: 
        if len(nums) < 2 or k == 1:
            return nums

        window, res = [], []
        for i, n in enumerate(nums):
            # 当前元素 > windows 最右边的值，将 window 最右边的值自右边推出
            while window and nums[window[-1]] <= n:
                window.pop()
            window.append(i)  # 添加当前值的索引
            # 如果索引大于 k 时，表示窗口已经建成，将最大值（最左边）添加到结果集中
            # 同时要判断 window 最左边的值，是不是已经不属于窗口了
            if i + 1 >= k:
                # 如果index + 1 - window[0]大于k时，
                # 说明window[0]已经不属于当前窗口了，所以从左边推出
                if window and i + 1 - window[0] > k:
                    window.pop(0)

                res.append(nums[window[0]])
        return res
```

#### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()


### 方法 3: 双向队列（use deque）

#### 思路

* 

```python
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # # 3. 双向队列（use deque）
        if len(nums) < 2 or k == 1:
            return nums

        res = []
        dq = collections.deque()
        for i, n in enumerate(nums):
            # 保证从大到小 如果前面数小则需要依次弹出，直至满足要求
            while dq and nums[dq[-1]] <= n:
                dq.pop()
            dq.append(i)
            # 判断队首是否有效
            if dq[0] <= i - k:
                dq.popleft()
            # 当窗口长度为 k，保存队首元素
            if i + 1 >= k:
                res.append(nums[dq[0]])
        return res
```

#### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()


### 方法 4: 使用大顶堆

#### 思路

* 

```python

```

#### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()
