# 69. x 的平方根: 

[69. x 的平方根](https://leetcode-cn.com/problems/sqrtx/)

```
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
```
## 方法 1: 二分查找法

### 思路

* 首先要明白，为什么这题可以使用「二分查找」算法来求解？
    * 二分查找适用于 **有序**、**有边界** 的数组搜索
    * 而本题要求 `x` 的平方根，且 `x >= 0`
        * 也即在二次函数 `y = x ^ 2` 中，给定一个 `y` 值，求解对应的 `x` 值
        * 而二次函数 `y = x ^ 2` 的图像当 `x >= 0` 时，为 **递增的** 
        * 且有 **上下界**，下界为 `0`，下界为 `x`
    * 所以本题可以用二分查找来求解
* 利用 **二分查找** 模板
    * 左边界 `low` 设为 `0`
    * 右边界 `high` 就设为 `x` 就可以了，也可以设为 x 的一半再加 1，但也只不过就多一次折半的运算而已。
    * 

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x in {0, 1}:
            return x

        low, high = 0, x // 2 + 1
        res = -1
        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= x:
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res
             
```

### 复杂度分析

* 时间复杂度：O(logx)
* 空间复杂度：O(1)


## 方法 2: 使用牛顿迭代法

### 思路

* 牛顿迭代法的思想是从一个初始近似值开始，然后作一系列改进的逼近根的过程。

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x in {0, 1}:
            return x

        # 2. 用牛顿迭代法
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)
```

### 复杂度分析

* 时间复杂度：O(logx)
    * 此方法是二次收敛的，相较于二分查找更快。
* 空间复杂度：O(1)

## 方法 3: 对上述牛顿迭代法进行精简

### 思路

* 参考：[3-4 short lines, Integer Newton, Every Language](https://leetcode.com/problems/sqrtx/discuss/25057/3-4-short-lines-Integer-Newton-Every-Language)

#### Python

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x in {0, 1}:
            return x

        # 3. 用精简牛顿迭代法
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return r
```

#### Go

```go
func mySqrt(x int) int {
    if x == 0 || x == 1 {
        returrn x
    }

    r := x
    for ; r * r > x ; {
        r = (r + x / r) / 2
    }
    return r
}
```


### 复杂度分析

* 时间复杂度：O(logx)
* 空间复杂度：O(1)

