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


### 方法 3: 暴力解法

#### 思路

* 要求 x 的 n 次幂，也就是让 x 乘上 n 次
* 可以通过简单的循环来实现，但在 LC 上通过不了，超时了。

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # bruce force - (timeout)
        if n == 0: return 1
        if n == 1: return x

        if n < 0:
            n = -n
            x = 1 / x

        res = 1
        for _ in range(n):
            res *= x

        return res
```

#### 复杂度分析

* 时间复杂度：O(n)
    * 要乘以 n 次
* 空间复杂度：O(1)


### 方法 4: 使用分治法

#### 思路

* 举例说明：x 的 10 次方，可以把 x 乘以 10 次；也可以用 x^5 乘以 x ^ 5 来得到
* 所以可以采用「分治」的方法，分治怎么解呢？
    * 就是把问题转成「子问题」，写程序时就是「递归」
    * 递归模板有四步：
        * 终止条件
        * 处理，而在分治里就是「拆分原有问题」
        * 下探到下一级，在这里就是「调用函数去做子问题」，再加上「合并子问题」
        * 清理状态
* 原有问题: `pow(x, n)`
* 子问题：`pow(x, n // 2)`
* 合并时：要区分奇偶性

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 分治
        def quickPow(x, n):
            # terminator
            if n == 0:
                return 1.0

            # drill down (split)
            half = quickPow(x, n // 2)

            # process (merge)
            # 下面 4 句也可简写为:
            # return half * half if n % 2 == 0 else half * half * x
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            x, n = 1 / x, -n

        return quickPow(x, n)
```

#### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()



### 方法 5: 另一种分治法

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