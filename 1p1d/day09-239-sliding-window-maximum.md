# day09: 239. 滑动窗口最大值 

[239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)

```

```
## Python

### 方法 1: 暴力解法

#### 思路

* 遍历 (0, n - k)，获取当前窗口内最大值，添加到结果集中

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 1. 暴力解法
        # i -> (0, n - k)
        res = []
        for i in range(len(nums) - k + 1):
            maxv = max(nums[i: (i + k)])
            res.append(maxv)

        return res
```

#### 复杂度分析

* 时间复杂度：O(n)
    * 遍历时间：O(n)
    * 取最大值：O()  ?
* 空间复杂度：O(n)


### 方法 2: 使用单调双向队列

#### 思路

* 

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 2. 使用单调的双向队列
        # 该双向队列，最左为最大，自左向右依次减小
        # 队列中存储的是元素的索引，不是元素的值
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
