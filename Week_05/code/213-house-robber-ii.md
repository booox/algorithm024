# 213. 打家劫舍 II: 

[213. 打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii/)

```
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

 

示例 1：

输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2：

输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 3：

输入：nums = [0]
输出：0
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 1000
```
## 方法 1: 使用动态规划

### 思路

* 本题为 [198. 打家劫舍](code/198-house-robber.md) 的升级版，区别在于 **首尾相连**
* 也就意味着 第一个元素，与第后一个元素只能选择其中之一，或者两者都不选
    * 可以将此题转换为第一题，求以下两种情况下的最大值
        * 第 0 个 元素不选：`nums[1:]`
        * 第 后一个 元素不选：`nums[:n-1]` ，n 为 nums 长度.
* 在解单数组时，定义了一个函数，并使用了两个单变量的方式

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size <= 2:
            return max(nums)

        def robber(nums):
            pre, curr = nums[0], max(nums[0], nums[1])

            for i in range(2, len(nums)):
                pre, curr = curr, max(curr, pre + nums[i])
            return curr

        return max(robber(nums[1:]), robber(nums[:size - 1]))
```

### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(1)
