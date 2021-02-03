# day10: 1021. 删除最外层的括号

[1021. 删除最外层的括号](https://leetcode-cn.com/problems/remove-outermost-parentheses/)

```

```
## Python

### 方法 1: 单指针

#### 思路

* 用指针 count 来对括号计数，遍历所有符号，按如下顺序进行处理
    * 遇到 ")"，count 减 1
    * 当 count 大于等于 1 时，将当前符号添加到结果集中
    * 遇到 "("，count 加 1；遇到右括号，减 1

```python
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        res = ""
        for c in S:
            if c == ")":
                count -= 1
            if count >= 1:
                res += c
            if c == "(":
                count += 1
        return res
```

#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(n)


### 方法 2: 单指针计数

#### 思路

* 要区分「最外层括号」与「非最外层括号」
* 可以设置一个计数器 count，初始为 0，来对遇到的括号计数
* 在每次计数之前，先判断一下是否为「非最外层括号」
    * 当 count 大于 0 时，遇到的 '('
    * 当 count 大于 1 时，遇到的 ')'


```python
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ""
        count = 0
        for c in S:
            if c == '(' and count > 0:
                res += c
            elif c == ')' and count > 1:
                res += c
            count += 1 if c == '(' else -1
        return res
```

#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(n)

### 方法 3: 使用栈

#### 思路

* [解法](https://leetcode-cn.com/problems/remove-outermost-parentheses/solution/shuang-zhi-zhen-ji-shu-fa-by-simzhou/)
* 碰到 "(" 就入栈，碰到 ")" 就消掉栈顶的一个 "(" 。
* 如果栈为空，那么刚刚碰到的 “)” 就是最外层右括号；如果入栈前栈为空，则即将入栈的 “(” 就是最外层左括号。
* 借助栈来判断，把非外层括号放进答案中。

```python
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        # use stack
        stack, res = [], ""
        for c in S:
            if c == "(":
                if stack: 
                    res += c
                stack.append(c)
            elif c == ")":
                stack.pop()
                if stack: 
                    res += c
        return res
```

#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(n)

