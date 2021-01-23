
# [412. Fizz Buzz](https://leetcode-cn.com/problems/fizz-buzz/)


```
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例：

n = 15,

返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
```

## Python

### 预备知识

* 求余的方法：`%`
* 逻辑表达式的书写
* 循环
* 判断
* 列表理解


### 思路分析

* 判断对应的字符串，主要用到了 `%` 求余这个操作符的用法
* 1 到 n 个数字，可以通过一次循环来迭代获取对应的输出字符串
    * 可以先生成 1~n 对应的数组，然后迭代
    * 也可以通过生成器


### Code 1

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        nums = list(range(1, n + 1))

        res = []
        for i in nums:
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(f"{i}")
        return res
```

#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(1)


### Code 2

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def fz(i):
            if i % 3 == 0 and i % 5 == 0:
                return "FizzBuzz"
            elif i % 3 == 0:
                return "Fizz"
            elif i % 5 == 0:
                return "Buzz"
            else:
                return f"{i}"  

        return [fz(i) for i in range(1, n + 1)]
```

#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(1)