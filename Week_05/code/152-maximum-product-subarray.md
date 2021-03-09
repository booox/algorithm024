# 152. 乘积最大子数组: 

[152. 乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray/)

```
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

 

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
```
## 方法 1: 动态规划

### 思路

* 本题与 [最大子序和](code/53-maximum-subarray.md) 类似，也是求解 **最优解** ，考虑使用动态规划
* 设定 `maxDP` 为动态数组，则 `maxDP[i]` 表示在 `i`位置，连续子数组的最大乘积。
    * 同时因为元素可能为负，而 **最小** 的负数，与负数相乘，可能变成最大的
    * 所以还需要再设一个 `minDP` 数组，保存 `i` 位置连续子数组的最小乘积
* 那对于 `i` 元素，它的最大乘积则为以下三种情况的 **最大值**，同时考虑元素的 **正负性**:
    * `nums[i]` 自身
    * `nums[i] * maxDP[i - 1]`
    * `nums[i] * minDP[i - 1]`

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return
        size = len(nums)
        if size == 1:
            return nums[0]
            
        # 因为存在负数，可能负负得正，所以还需要保留一个最小的 dp 数组
        maxDP = [1 for _ in range(size)]
        maxDP[0] = nums[0]
        minDP = [1 for _ in range(size)]
        minDP[0] = nums[0]

        for i in range(1, size):
            maxDP[i] = max(nums[i], nums[i] * maxDP[i - 1], nums[i] * minDP[i - 1])
            minDP[i] = min(nums[i], nums[i] * maxDP[i - 1], nums[i] * minDP[i - 1])

        return max(maxDP)
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()
