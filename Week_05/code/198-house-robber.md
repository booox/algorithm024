# 198. 打家劫舍: 

[198. 打家劫舍](https://leetcode-cn.com/problems/house-robber/)

```
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
 

提示：

0 <= nums.length <= 100
0 <= nums[i] <= 400
```
## 方法 1: 动态规划，二维数组

### 思路

* 考虑二维 dp 数组
* `dp[i]` 表示从 0..i 可以偷到的最高金额
    * `dp[i][0]` 表示，不偷 `i` 房间
    * `dp[i][1]` 表示，偷 `i` 房间
* 当只有一个房间时：
    * 不偷: `dp[0][0] = 0`
    * 偷: `dp[0][1] = nums[0]`
* 第 `i` 个房间：
    * 不偷: `dp[i][0]`，应为第 `i - 1` 房间，**偷** 与 **不偷** 中最大的
    * 偷: `dp[i][1]`，应为第 `i - 1` 个房间**不偷**，再加上 `nums[i]`

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size == 1:
            return nums[0]

        # dp[i]: 表示从 0..i 可以偷到的最高金额
        dp = [[0, 1] for _ in range(size)]
        dp[0][0] = 0
        dp[0][1] = nums[0]
        

        for i in range(1, size):
            # nums[i] 不选
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            # nums[i] 选
            dp[i][1] = dp[i - 1][0] + nums[i]

        return max(dp[size - 1][0], dp[size - 1][1])
```

### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(n)



## 方法 2: 动态规划，一维数组

### 思路

* 使用一维数组
* `dp[i]`: 表示从 0..i 可以偷到的最高金额
* 基本情况：
    * 只有一个房间，`dp[0]`，那就是 `nums[0]`了
    * 只有两个房间，`dp[1]`，那就是 `nums[0]` 与 `nums[1]` 中最大者
* 第 `i` 个房间，`dp[i]`，应为下面两者较大者：
    * 第 `i - 1` 个房间可以偷到的最高金额
    * 第 `i - 2` 个房间可以偷到的最高金额，再加上 `nums[i]`

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size == 1:
            return nums[0]

        # dp[i]: 表示从 0..i 可以偷到的最高金额
        dp = [0 for _ in range(size)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        

        for i in range(2, size):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[size - 1]
```

### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(n)


## 方法 3: 动态规划，数组压缩

### 思路

* 思路同方法 2，但不再额外使用数组，而是使用两个变量


```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size == 1:
            return nums[0]

        pre, curr = nums[0], max(nums[0], nums[1])

        for i in range(2, size):
            # dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            pre, curr = curr, max(curr, pre + nums[i])
       
        # pre, curr = 0, 0
        # for i in range(size):
        #     pre, curr = curr, max(curr, pre + nums[i])

        return curr
```

### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(1)


