
# 66. 加一 

[66. 加一](https://leetcode-cn.com/problems/plus-one/)

## 解法

* 使用双指针

```
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
示例 2：

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
示例 3：

输入：digits = [0]
输出：[1]
```


## Python

### 方法 1：

#### 思路

* 添加前置 0，用于判断是否进位到最高位
* 逢 9 加一进一


```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 添加前置 0，用于判断是否进位到最高位
        # 逢 9 加一进一

        digits = [0] + digits
        for i in range(len(digits) - 1, -1, -1):
            # 如果该位不为 9，则直接加 1，结束循环
            if digits[i] != 9:      
                digits[i] += 1
                break
            else:   # 如果为 9，只需将该位设为 0
                digits[i] = 0

        return digits[1:] if digits[0] == 0 else digits
```


#### 复杂度分析

* 时间复杂度：O(n)
* 空间复杂度：O(1)

