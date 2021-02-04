# day11: 412. Fizz Buzz

[412. Fizz Buzz](https://leetcode-cn.com/problems/fizz-buzz/)

```

```
## Python

### 方法 1: 暴力遍历，判断

#### 思路

* 直接暴力遍历每个数，判断每个数对应的情况，将结果添加到结果集中

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # 1. 暴力遍历
        res = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))

        return res
```

#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(1)
    * 每次都只取一个数来进行「操作」，所以空间复杂度为 O(1)


### 方法 2: 还是暴力，构造判断函数，使用列表理解

#### 思路

* 将判断过程构造为函数
* 使用「列表的理解」来提速

```python

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # 2. 还是暴力，只是将判断写成函数，并使用列表的理解
        def fz(i):
            if i % 3 == 0 and i % 5 == 0:
                return "FizzBuzz"
            elif i % 3 == 0:
                return "Fizz"
            elif i % 5 == 0:
                return "Buzz"
            else:
                return str(i)

        return [fz(i) for i in range(1, n + 1)]
```

#### 复杂度分析

* 时间复杂度：O(n)
    * 要遍历判断 n 个数
* 空间复杂度：O(1)

### 方法 3: 字符串连接

#### 思路

* 这个方法不会降低渐进复杂度，但是当 FizzBuzz 的规则变得更复杂的时候，这将会是个更优雅的解法。
* 比方说，玩个 FizzBuzzJazz 的游戏。 `3 ---> "Fizz" , 5 ---> "Buzz", 7 ---> "Jazz"`
    * 就是分别判断：
        * 如果这个数能被 3 整除，就把 "Fizz" 连接到结果字符串中
        * 如果这个数能被 5 整除，就把 "Buzz" 连接到结果字符串中
        * 如果这个数能被 7 整除，就把 "Jazz" 连接到结果字符串中


```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # 3. 连接字符串
        def fz(i):
            ans = ""
            if i % 3 == 0:
                ans += "Fizz"
            if i % 5 == 0:
                ans += "Buzz"
            return str(i) if ans == "" else ans


        return [fz(i) for i in range(1, n + 1)]
```

#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(1)


### 方法 4: 使用哈希表

#### 思路

* 该方法是对方法 3 的优化，可以将需要整除的数作为 key 及对应的字符存入哈希表当中

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # 4. 使用哈希表
        fzhash = {3: "Fizz", 5: "Buzz"}
        def fz(i):
            ans = ""
            for key, value in fzhash.items():
                if i % key == 0:
                    ans += value
            return str(i) if ans == "" else ans
        
        return [fz(i) for i in range(1, n + 1)]
```

#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(1)
