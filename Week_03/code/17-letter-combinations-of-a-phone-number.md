# 17. 电话号码的字母组合: 

[17. 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)

```
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



 

示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
示例 3：

输入：digits = "2"
输出：["a","b","c"]
 

提示：

0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。
```
## Python

### 方法 1: 

#### 思路

* 与前面 [括号生成](../Week_02/code/22-generate-parentheses.md) ([leetcode](https://leetcode-cn.com/problems/generate-parentheses/)) 类似
    * 先将数字对应的字母放入哈希表当中
    * 对于 digits 数字串来说，可以将每个数字的位置想像成一个格子
        * 每个格子，可以有多种摆放方法（即对应的字母）
    * 每次处理一个数字
        * 获取该数字对应的字母
        * 依次将字母添加到 **已有** 字母的字符串的后面
        * 接着处理后一位数字，直到处理完所有数字
        * 得到一个完整的字母列表
    * 回退，处理其余字母
* 使用回溯算法

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        chars_map = {
            '2': "abc", 
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }
        if len(digits) == 0:
            return []

        res = []
        self.__dfs(digits, chars_map, 0, "", res)
        return res

    def __dfs(self, digits, chars_map, depth, path, res):
        # terminator: 当深度等于 digits 长度时，进行结算
        if depth == len(digits):
            res.append(path)
            return

        # process
        # 获取数字对应的字母
        chars = chars_map[digits[depth]]
        for i in range(len(chars)):
            # drill down
            # 下探到下一层
            self.__dfs(digits, chars_map, depth + 1, path + chars[i], res)


        # revert states

```

#### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()


### 方法 2: 使用队列

#### 思路

* 先将

```python

```

#### 复杂度分析

* 时间复杂度：O()
* 空间复杂度：O()
