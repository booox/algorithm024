# 121. 买卖股票的最佳时机: 

[121. 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)

```
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

 

示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
 

提示：

1 <= prices.length <= 105
0 <= prices[i] <= 104   
```
## 方法 1: 使用暴力解法 - 会超时

### 思路

* 可以使用暴力解法，使用双指针，i 从 (0, n - 1)； j 在  (i + 1, n)
* 先初始化结果为 `float('-inf')` ，然后依次统计每次交易的值，并与结果比较，更新为最大者
* 最后将结果输出，还需要考虑一下，若没有利润，则输出 `0`


```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # 1. brute force
        # 遍历统计每次交易所能获得的利润，找到最大的
        res = float('-inf')

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                res = max(res, prices[j] - prices[i])

        return res if res > 0 else 0
```

### 复杂度分析

* 时间复杂度：O(n^2)
* 空间复杂度：O(1)

## 方法 2: 使用动态规划

### 思路

* 求最优化解，考虑使用动态规划
* 初始化 `dp` 数组全部为 `0`
* 设定买入价 `buy` 为第 0 个元素
* 从索引为 1 的元素开始遍历，直到最后，若有利润则更新
    * 若有利润，则更新 dp[i]
    * 若无利润，说明当前价格小于前面的买入价，将买入价设为当前价格


```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # # 求最大利润，最优化的操作，考虑使用动态规划
        size = len(prices)
        dp = [0 for _ in range(size)]
        buy = prices[0]

        for i in range(1, size):
            # dp[i]: 表示在 i 点，所能获得的最大利润
            if prices[i] > buy:
                dp[i] = max(dp[i - 1], prices[i] - buy)
            else:
                buy = prices[i]
        return max(dp)
```

### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()


## 方法 3: 一次遍历

### 思路

* 只考虑每天的最低价格，及所能获得的最大利润
* 最后将最大利润返回即可。

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # 3. 一次遍历，考虑每天最低价格，及所能获得的最大利润
        min_price, max_profit = float('inf'), 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
```

### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(1)
