# 367. 有效的完全平方数: 

[367. 有效的完全平方数](https://leetcode-cn.com/problems/valid-perfect-square/)

```
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False
```


## 方法 1: 二分查找

### 思路

* num 的范围为正整数，1 是完全平方数，从 2 开始，到 num 之间整数为 **递增**，且有 **边界**，所以可以用 **二分查找**
* 直接套模板

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        # 1. 二分查找
        low, high = 1, num
        while low <= high:
            mid = int(low + (high - low) / 2)
            if mid * mid == num:
                return True
            elif mid * mid > num:
                high = mid - 1
            else:
                low = mid + 1
        return False
```

### 复杂度分析

* 时间复杂度：O(logn)
* 空间复杂度：O(1)

## 方法 2: 使用牛顿迭代法

### 思路

* 与 [x 的平方根](code/69-sqrtx.md) 类似，一样可以使用牛顿法
* 算法：
    * 我们取 `num/2` 作为初始近似值。
    * 当 `x * x > num`，用牛顿迭代法取计算下一个近似值：`x = 1/2(x + num / x)`
* 返回 x*x == num。


```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        # 2. 牛顿法
        # 取 `num/2` 作为初始近似值。
        x = num // 2
        # 当 x * x > num 时，迭代逼近根
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num
```

### 复杂度分析

* 时间复杂度：O(logn)
* 空间复杂度：O(1)

