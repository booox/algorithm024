# 50. Pow(x, n): 

[50. Pow(x, n)](https://leetcode-cn.com/problems/powx-n/)

```
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。

 

示例 1：

输入：x = 2.00000, n = 10
输出：1024.00000
示例 2：

输入：x = 2.10000, n = 3
输出：9.26100
示例 3：

输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25
 

提示：

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
```
## Python

### 方法 1: 调用库（偷懒^-^）

#### 思路

* 现成工具真好用，但不利于锻炼思维
* 可以用 `math.pow()`， 或直接使用 `pow()`

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 1. use math.pow
        import math
        return math.pow(x, n)

        # 2. use pow
        # return pow(x, n)
```

#### 复杂度分析

* 时间复杂度：O(1)
* 空间复杂度：O(1)

### 方法 2: 使用指数运算符

#### 思路

* 

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n
```

#### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()



### 方法 3: 使用二分法

#### 思路

* 在纸上画一下，将 n 依次折半（整除 2），直到 变成 0
    * curr 初始为 x
    * curr *= curr
* 当 n 对 2 求余为 1 时，将 curr 乘到结果中
* 要注意当 n < 0 时的处理

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 2. binary search
        if n == 0: return 1
        if n == 1: return x

        if n < 0:
            n = -n
            x = 1 / x
        
        curr, res = x, 1.0
        while n > 0:
            # if n % 2 == 1:
            if n % 2:       # 这样似乎更快一些
                res *= curr
            curr *= curr
            n = n // 2

        return res
```

#### 复杂度分析

* 时间复杂度：O(logn)
* 空间复杂度：O(1)


### 刷题时要思考什么？

1. 要理解题意，输入输出分别是什么？
2. 思考有哪几种方法处理？
    * 已有库是否可以解决？
    * 暴力解法呢？
    * 是否有现成模板？
3. 分析不同方法的复杂度
4. 考虑边界情况
5. 提交之前，再检查一下代码