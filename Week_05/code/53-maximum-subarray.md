# 53. 最大子序和: 

[53. 最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)

## 补充知识

* 求 **最大子序列和** 在以下方面有实际的应用：
    * **基因测序**
    * **计算机视觉**，可以用于检测一张图片中最亮的那个区域。

## 类似题目

* [121. 买卖股票的最佳时机](code/) [leetcode](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock)

```
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

 

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [0]
输出：0
示例 4：

输入：nums = [-1]
输出：-1
示例 5：

输入：nums = [-100000]
输出：-100000
 

提示：

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
 

进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
```
## 方法 1: 动态规划 

### 思路

* 这是一个 **求最优解** 的问题，它通常可以用 **动态规划 DP** 来求解。
* 要用 **DP**，第一件事就是要找出 **子问题的格式（或子问题的状态）**。
    * 假设只有一个元素，则最大子序列和就是它本身；
    * 再加一个元素，则最大子序列和就是，下面两者取最大值：
        * 当前元素
        * 上一子序列和与当前元素和
    * 继续递推
* dp[i]: 表示到 i 点，最大的连续子数组和，


* 参考

> Apparently, this is a optimization problem, which can be usually solved by DP. So when it comes to DP, the first thing for us to figure out is the format of the sub problem(or the state of each sub problem). The format of the sub problem can be helpful when we are trying to come up with the recursive relation.

> 显然，这是一个 **求最优解** 的问题，它通常可以用 **动态规划 DP** 来求解。
> 既然讲到了 **DP**，第一件事就是要找出 **子问题的格式（或子问题的状态）**


```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        dp = [0] * size
        # dp[i]: 到 i 点，最大的连续子数组和

        for i in range(size):
            # nums[i] 有两种可能：
            # 与前面的连在一起，或新开一个子数组 
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        return max(dp)
```

**或直接在 nums 上修改**


```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return

        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])

        return max(nums)
```


### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(n)


## 方法 2: 动态规划 - 压缩空间

### 思路

* 思路同方法 1，只是考虑到每次 dp 方程转移时只与前一个 **子序列和** 相关，所以可以略去使用一维数组


```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = nums[0]
        res = float('-inf')

        for i in range(1, len(nums)):
            dp = max(nums[i], dp + nums[i])
            res = max(res, dp)

        return res
```

### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(1)



## 方法 3: 抄自国际站

### 思路

* 参考： [it is a game of sum, not the elements.](https://leetcode.com/problems/maximum-subarray/discuss/20396/Easy-Python-Way/236689)
* 简单来说，就是如果对 **子序列和** 增大有帮助就加，否则就重新统计，最后返回最大值。
* 如果 **子序列和** 为 **正**，则它对 **子序列和** 变大有帮助，就持续这个操作直到它变为负的。
* 如果 **子序列和** 为负，则它对让 **子序列和** 变大没有贡献，所以停止当前序列继续下一个子序列。


```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        
        return max(nums)
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()


## 方法 : 

### 思路

* 

```python

```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()
