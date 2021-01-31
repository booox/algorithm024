# 1. 两数之和

[1. 两数之和](https://leetcode-cn.com/problems/two-sum/)

```
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
 

提示：

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案

```
## Python

### 方法 1：暴力解法

#### 思路

* 使用两层循环
    * 外层循环，依次从数组中取一个元素
    * 内层循环，负责在取得的元素右侧查找
    * 若二者之和等于 target，则返回对应的索引

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. 暴力
        # # i: 0, len - 2; 
        # # j: i + 1, len
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

#### 复杂度分析

* 时间复杂度：O(n^2)
* 空间复杂度：O(1)


### 方法 2: 使用哈希表

#### 思路

* 上述暴力方法使用了两次循环，是因为要在取得元素的右边，继续使用循环来遍历查找 `target - n`，时间复杂度为 `O(n)`，合在一起为 `O(n^2)`
* 可以考虑使用哈希表，来实现基于 `O(1)` 的查找
* 这里降低了时间复杂度，但提升了空间复杂度，运用了 **用空间换时间** 的思想


```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2. 使用哈希表
        d = {}
        for i, n in enumerate(nums):
            if target - n in d:
                return [d[target -n], i]
            else:
                d[n] = i
```

#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(n)
