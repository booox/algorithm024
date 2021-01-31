# 283. 移动零

[283. 移动零](https://leetcode-cn.com/problems/move-zeroes/)

```
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

```
## Python

### 方法 1: 使用双指针（不满足题意）

#### 思路 

* 一个指针负责遍历所有元素，另一指针负责记录非零元素最后的索引
* 当遇到不等于 0 的元素时，就将对应的值，赋给非零索引
* 最后再填充 0


```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. 使用双指针
        idx, size = 0, len(nums)
        for i in range(size):
            if nums[i] != 0:
                nums[idx] = nums[i]
                idx += 1
            
        # 这种方法是不满足题意的
        nums[idx:] = [0] * (size - idx)
        # 想知道的是：它的空间复杂度是多少？ O(n)

        # 空间复杂度为 O(1)，但这样还是把题目复杂化了
        for i in range(idx, size):
            nums[i] = 0
```

#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(1)

### 方法 2：双指针（交换位置）

#### 思路

* * 看到 **保持非零元素的相对顺序**，要想到可以使用「栈或快慢指针」
* 看到 **必须在原数组上操作**，即空间复杂度要求 `O(1)`，所以要用「快慢指针」

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2. 使用双指针
        size = len(nums)
        idx, size = 0, len(nums)

        for i in range(size):
            if nums[i] != 0:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1


        # 3. 使用双指针，变量命名更有意义
        slow, fast = 0, 0

        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
```

#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(1)
