
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

### 方法 1：使用双指针

#### 思路

* 可以考虑使用双指针
    * 快指针：遍历所有元素
    * 慢指针：记录非零元素位置
    * 当检测到非零元素之后，就将它向前移
    * 最后再将剩余元素赋值为 0 

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 使用双指针
        # # 慢指针记录非零元素位置；快指针用于遍历
        zero = 0
        for i, n in enumerate(nums):
            if n != 0:
                nums[zero] = n
                zero += 1

        nums[zero:] = [0] * (len(nums) - zero)
```


#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(1)

